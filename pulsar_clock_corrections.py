"""Maintain up-to-date clock corrections."""
import inspect
import re
import tempfile
from io import StringIO
from pathlib import Path
from textwrap import dedent, indent
from typing import List, Optional, Iterable, Union

import astropy.units as u
import numpy as np
from astropy.time import Time
from astropy.utils.data import download_file
from pint.observatory.clock_file import ClockFile

import bipm
import iers

public_repo_url_raw = (
    "https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/"
)


def base_location() -> Path:
    return Path(__file__).parent


def list_candidate_clock_files() -> List[Path]:
    return sorted(base_location().glob("tempo/clock/time*_*.dat")) + sorted(
        base_location().glob("T2runtime/clock/*2*.clk")
    )


class ValidationError(RuntimeError):
    pass


class FileUpdater:
    def __init__(
        self,
        short_description: str,
        filename: str,
        authority: str = "temporary",
        invalid_if_older_than: Optional[Time] = None,
        update_interval_days: float = 7,
        description: str = "",
    ):
        self.filename = filename
        self.short_description = short_description
        self.filepath: Path = base_location() / self.filename
        self.authority = authority
        self.invalid_if_older_than = invalid_if_older_than
        self.update_interval_days = update_interval_days
        self.description = inspect.cleandoc(description)
        self._last_log_entry: Optional[str] = None
        self.log_entry_re = re.compile(r"([0-9 :.-]+) - ([^:]+)(: (.*))?")
        self.interval_fuzz: u.Quantity = 1 * u.hour
        self._clock_file = None
        self._tstart = None
        self._tend = None

    @property
    def tstart(self):
        return self._tstart

    @property
    def tend(self):
        return self._tend

    def needs_update(self):
        """Check whether the update process needs to run.

        This normally involves checking the current time against
        the update schedule, but subclasses may override this
        (for example checking whether other files have changed
        recently).
        """
        try:
            t, r, m = self.parse_log_entry(self.last_log_entry)
        except FileNotFoundError:
            # Never looked before, go ahead
            return True
        else:
            return (Time.now() - t).sec > (
                self.update_interval_days * u.day - self.interval_fuzz
            ).to_value(u.s)

    @property
    def log_file(self):
        return base_location() / "log" / f"{self.filename}.log"

    def add_to_log(self, msg):
        entry = f"{Time.now().iso} - " + msg.replace("\n", " ") + "\n"
        with open(self.log_file, "at") as f:
            f.write(entry)
        self._last_log_entry = entry

    @property
    def last_log_entry(self) -> str:
        if self._last_log_entry is None:
            self._last_log_entry = open(self.log_file, "rt").readlines()[-1]
        return self._last_log_entry

    def parse_log_entry(self, entry):
        r = self.log_entry_re.match(entry.strip())
        reason = r.group(4)
        if reason is None:
            reason = ""
        return Time(r.group(1), format="iso"), r.group(2), reason

    def get(self, cache=False) -> Path:
        raise NotImplementedError

    def validate(self, new_file):
        raise NotImplementedError

    def try_update(self, cache=False, respect_interval=True, force=False):
        if not force and respect_interval and not self.needs_update():
            # No new data to be had, no log entry
            return True
        try:
            f = self.get(cache=cache)
        except IOError as e:
            self.add_to_log(f"Failed to download: {e}")
            return False
        new_contents = Path(f).read_text()
        try:
            old_contents = self.filepath.read_text()
        except FileNotFoundError:
            pass
        else:
            if old_contents == new_contents:
                self.add_to_log("Unchanged")
                return True
            try:
                self.validate(f)
            except ValidationError as e:
                self.add_to_log(f"Validation failed: {e}")
                if not force:
                    return False
        self.filepath.write_text(new_contents)
        self._clock_file = None
        if force:
            self.add_to_log("Updated overriding validation failure")
        else:
            self.add_to_log("Updated")
        return True

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.short_description!r}, {self.filename!r})"
        )


class ClockFileUpdater(FileUpdater):
    def __init__(
        self,
        short_description: str,
        filename: str,
        authority: str = "temporary",
        download_url: Optional[str] = None,
        format: str = "tempo",
        bogus_last_correction: bool = False,
        obscode: Optional[str] = None,
        invalid_if_older_than: Time = None,
        update_interval_days: float = 7,
        description: str = "",
    ):
        super().__init__(
            short_description,
            filename,
            authority=authority,
            invalid_if_older_than=invalid_if_older_than,
            update_interval_days=update_interval_days,
            description=description,
        )
        self.format = format
        self.bogus_last_correction = bogus_last_correction
        self.download_url = download_url
        self.obscode = obscode
        self._last_log_entry: Optional[str] = None
        self.log_entry_re = re.compile(r"([0-9 :.-]+) - ([^:]+)(: (.*))?")

    def get(self, cache=False):
        if self.download_url is not None:
            return Path(download_file(self.download_url, cache=cache))
        self.add_to_log(f"No way to download: {self.filename!r}")
        return None

    @property
    def clock_file(self):
        if self._clock_file is None:
            if self.obscode is not None:
                self._clock_file = ClockFile.read(
                    str(base_location() / self.filename),
                    format=self.format,
                    bogus_last_correction=self.bogus_last_correction,
                    obscode=self.obscode,
                )
            else:
                self._clock_file = ClockFile.read(
                    str(base_location() / self.filename),
                    format=self.format,
                    bogus_last_correction=self.bogus_last_correction,
                )
        return self._clock_file

    @property
    def tstart(self):
        if self.clock_file is None or len(self.clock_file.time) == 0:
            return None
        return self.clock_file.time[0]

    @property
    def tend(self):
        if self.clock_file is None or len(self.clock_file.time) == 0:
            return None
        return self._clock_file.time[-1]

    def validate(self, new_file):
        old = self.clock_file
        try:
            if self.obscode is not None:
                new = ClockFile.read(
                    str(new_file),
                    format=self.format,
                    bogus_last_correction=self.bogus_last_correction,
                    obscode=self.obscode,
                )
            else:
                new = ClockFile.read(
                    str(new_file),
                    format=self.format,
                    bogus_last_correction=self.bogus_last_correction,
                )
        except ValueError as e:
            raise ValidationError(
                f"Unable to read new version of {self.filename}: {e}"
            ) from e
        if len(old.time) > len(new.time):
            raise ValidationError(
                f"New version of {self.filename} has decreased from {len(old.clock)} "
                f"to {len(new.clock)} measurements."
            )
        d = old.time != new.time[: len(old.time)]
        if np.any(d):
            raise ValidationError(
                f"New version of {self.filename} MJDs differ from old "
                f"version where they overlap in {np.sum(d)} places"
            )
        if len(old.clock) > 0:
            d = old.clock[:-1] != new.clock[: len(old.clock) - 1]
        else:
            d = old.clock != new.clock[: len(old.clock)]
        if np.any(d):
            raise ValidationError(
                f"New version of {self.filename} clock corrections differ from old "
                f"version where they overlap in {np.sum(d)} places"
            )

    def details_page(self, make_plots_in_dir: Optional[Path] = None) -> str:
        # Just ensure that this was loaded
        self.clock_file

        last_date, result, details = self.parse_log_entry(self.last_log_entry)
        log_url = f"{public_repo_url_raw}log/{self.filename}.log"

        f = StringIO()
        f.write(
            dedent(
                f"""
                ## {self.short_description}

                """
            )
        )
        f.write(self.description)
        f.write(
            dedent(
                f"""

                |     |     |
                |:--- |:--- |
                | File | `{self.filename}` |
                | Authority | {self.authority} |
                | URL in repository | <{public_repo_url_raw + self.filename}> |
                | Original download URL | <{self.download_url}> |
                | Format | {self.format} |
                | Bogus last correction | {self.bogus_last_correction} |
                | Clock file start | {short_date_and_mjd(self.tstart)} |
                | Clock file end | {short_date_and_mjd(self.tend)} |
                | Update interval (days) | {self.update_interval_days} |
                | Last update attempt | {short_date(last_date)} |
                | Last update result | {result} |

                Log entries from the last few update attempts:
            """
            )
        )
        f.write("```\n")
        for line in self.log_file.open().readlines()[-10:]:
            f.write(line)
        f.write("```\n")
        f.write(f"[Full log]({log_url})\n")
        if self.clock_file.leading_comment:
            self._write_leading_comment(f)
        if make_plots_in_dir:
            self._write_plot(make_plots_in_dir, f)
        return f.getvalue()

    def _write_plot(self, make_plots_in_dir: Path, f):
        import matplotlib.pyplot as plt
        from astropy.visualization import quantity_support

        quantity_support()

        size = (5, 2)
        plt.figure()
        plt.plot(self.clock_file.time.mjd, self.clock_file.clock.to(u.ns), ".")
        self._finalize_plot(plt, size)
        dpi = 144
        plt.savefig(make_plots_in_dir / f"{self.filename}.png", dpi=dpi)
        plt.close()

        plt.figure()
        n = 90
        plt.plot(
            self.clock_file.time.mjd[-n:], self.clock_file.clock[-n:].to(u.ns), "."
        )
        self._finalize_plot(plt, size)
        plt.savefig(make_plots_in_dir / f"{self.filename}.short.png", dpi=dpi)
        plt.close()
        f.write(
            dedent(
                f"""

                    All clock corrections:

                    ![plot of all clock corrections]({self.filepath.name}.png "All corrections")

                    Recent clock corrections:

                    ![plot of recent clock corrections]({self.filepath.name}.short.png "Recent corrections")

                    """
            )
        )

    # TODO Rename this here and in `_write_plot`
    def _finalize_plot(self, plt, size):
        plt.xlabel("MJD")
        plt.ylabel("corr. (ns)")
        plt.title(self.filename)
        plt.gcf().set_size_inches(size)
        plt.tight_layout()

    def _write_leading_comment(self, f):
        f.write("\n")
        f.write("Leading comments from clock file:\n")
        f.write("\n")
        f.write(indent(self.clock_file.leading_comment, 4 * " "))
        f.write("\n")
        f.write("\n")


class ClockFileConverterUpdater(ClockFileUpdater):
    def __init__(
        self,
        short_description,
        filename,
        updater,
        format="tempo2",
        hdrline="",
        description="",
    ):

        super().__init__(
            short_description,
            filename,
            authority="converted",
            format=format,
            update_interval_days=updater.update_interval_days,
            description=description,
        )

        # FIXME: allow merging
        self.hdrline = hdrline
        self.updater = updater

    def needs_update(self):
        """Check whether the converted file needs an update.

        Essentially we need to check whether the last update of this file is
        newer than the last update of the file it was converted from.
        """
        try:
            our_log = self.log_file.open().readlines()
        except IOError:
            return True
        try:
            other_log = self.updater.log_file.open().readlines()
        except IOError:
            # If *it* doesn't have a log file we're in trouble
            return True
        for e in our_log[::-1]:
            our_t, msg, _ = self.parse_log_entry(e)
            if msg.startswith("Updated"):
                break
        else:
            # Seems we've never updated the file
            return True
        for e in other_log[::-1]:
            other_t, msg, _ = self.parse_log_entry(e)
            if msg.startswith("Updated"):
                break
        else:
            # Seems we've never updated the other file?
            return True
        return our_t < other_t

    def get(self, cache=False):
        # combine self.updaters and write out an appropriate file
        # need to write this somewhere temporary but persistent enough to last until
        # it can be validated and used or discarded

        # FIXME: get should return contents not a filename

        filename = Path(tempfile.mkdtemp()) / "converted"

        # FIXME: this results in a changed file every time the update checker
        # is run, just because the conversion date is updated. We need to
        # check and do updates only if the source file has been updated.
        comments = (
            f"# This file was automatically converted from "
            f"{self.updater.filename} on {Time.now().iso}\n"
        )
        if self.format == "tempo2":
            self.updater.clock_file.write_tempo2_clock_file(
                str(filename),
                self.hdrline,
                extra_comment=comments,
            )
        else:
            raise ValueError(f"Unknown format {self.format}")

        return filename


class ClockFileCallableUpdater(ClockFileUpdater):
    def __init__(
        self,
        short_description,
        filename,
        authority,
        callable,
        update_interval_days=1,
        format="tempo2",
        description="",
    ):

        super().__init__(
            short_description,
            filename,
            authority=authority,
            format=format,
            update_interval_days=update_interval_days,
            description=description,
        )

        # FIXME: allow merging
        self.callable = callable

    def get(self, cache=False):
        # FIXME: get should return contents not a filename

        filename = Path(tempfile.mkdtemp()) / "converted"

        clock_file = self.callable()
        if self.format == "tempo2":
            clock_file.write_tempo2_clock_file(filename)
        else:
            raise ValueError(f"Unknown format {self.format}")

        return filename


class CallableUpdater(FileUpdater):
    """Updater for files that aren't clock files exactly."""

    def __init__(
        self,
        short_description,
        filename,
        authority,
        callable,
        update_interval_days=0,
        description="",
    ):

        super().__init__(
            short_description,
            filename,
            authority=authority,
            update_interval_days=update_interval_days,
            description=description,
        )

        self.callable = callable

    def get(self, cache=False):
        try:
            contents, tstart, tend = self.callable()
        except (IOError, ValueError) as e:
            self.add_to_log(f"Exception: Problem computing new value {e}")
            raise
        # FIXME: no way to get tstart/tend if there hasn't been a get()
        self._tstart, self._tend = tstart, tend
        filename = Path(tempfile.mkdtemp()) / "generated"
        filename.write_text(contents)
        return filename

    def validate(self, filename):
        # No idea what to check, sorry
        pass

    def details_page(self, make_plots_in_dir=None):
        last_date, result, details = self.parse_log_entry(self.last_log_entry)
        log_url = f"{public_repo_url_raw}log/{self.filename}.log"
        f = StringIO()
        f.write(
            dedent(
                f"""
                ## {self.short_description}

                """
            )
        )
        f.write(self.description)
        f.write(
            dedent(
                f"""

            |     |     |
            |:--- |:--- |
            | File | `{self.filename}` |
            | Authority | {self.authority} |
            | File start | {short_date_and_mjd(self.tstart)} |
            | File end | {short_date_and_mjd(self.tend)} |
            | Update interval (days) | {self.update_interval_days} |
            | Last update attempt | {short_date(last_date)} |
            | Last update result | {result} |

            Log entries from the last few update attempts:
            """
            )
        )
        f.write("```\n")
        for line in self.log_file.open().readlines()[-10:]:
            f.write(line)
        f.write("```\n")
        f.write(f"[Full log]({log_url})\n")

        return f.getvalue()


tempo_repository_url = (
    "https://sourceforge.net/p/tempo/tempo/ci/master/tree/clock/{}?format=raw"
)
tempo2_repository_url = (
    "https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/{}"
)

updaters: List[FileUpdater] = []


def get_updater(name: str) -> FileUpdater:
    for updater in updaters:
        if (
            updater.short_description.lower() == name.lower()
            or updater.filename == name
            or Path(updater.filename).name == name
        ):
            return updater
    raise ValueError(f"Unable to find an updater for {name}")


def try_all_updates(respect_interval=True):
    for updater in updaters:
        updater.try_update(respect_interval=respect_interval)
        print(f"{updater.short_description:20} {updater.last_log_entry.strip()}")


def short_date(t: Time) -> str:
    return "---" if t is None else t.datetime.strftime("%Y-%m-%d")


def short_date_and_mjd(t: Time) -> str:
    return "---" if t is None else f"{short_date(t)} MJD {t.mjd:.1f}"


def generate_index_txt():
    with open(base_location() / "index.txt", "wt") as f:
        print(f"{'# File':40s} {'Update (days)':13s}   Invalid if older than", file=f)
        for updater in updaters:
            print(
                f"{updater.filename:40s} {updater.update_interval_days:13.1f}   "
                f"{short_date(updater.invalid_if_older_than)}",
                file=f,
            )


def updater_summary_table(updaters: Iterable[FileUpdater], detail_urls=False) -> str:
    o = StringIO()
    print(
        "| Name "
        "| File "
        "| Corrections start "
        "| Corrections end "
        "| Last check date "
        "| Last check result ",
        file=o,
    )
    print("|:--- |:--- | --- | --- | --- |:--- ", file=o)
    for updater in updaters:
        last_date, result, details = updater.parse_log_entry(updater.last_log_entry)
        if (
            hasattr(updater, "download_url")
            and updater.download_url is None
            and not np.isfinite(updater.update_interval_days)
        ):
            result = "Static"
        elif result not in {"Unchanged", "Updated"}:
            result = f"**{result}**"

        detail_url = f"{updater.filename}.html"
        if detail_urls:
            print(
                f"| [{updater.short_description}]({detail_url}) "
                f"| `{updater.filename}` "
                f"| {short_date_and_mjd(updater.tstart)} "
                f"| {short_date_and_mjd(updater.tend)} "
                f"| {short_date(last_date)} "
                f"| {result} ",
                file=o,
            )
        else:
            print(
                f"| {updater.short_description} "
                f"| `{updater.filename}` "
                f"| {short_date_and_mjd(updater.tstart)} "
                f"| {short_date_and_mjd(updater.tend)} "
                f"| {short_date(last_date)} "
                f"| {result} ",
                file=o,
            )
    print(file=o)
    return o.getvalue()


class PagesUpdater:
    """Update the gh_pages site.

    The object should be pointed at a git repository with the gh_pages branch
    checked out. It will update the information there, overwriting the
    automatically generated files.
    """

    def __init__(self, directory: Union[Path, str]):
        self.directory = Path(directory)
        if not (self.directory / ".this_is_gh_pages").exists():
            raise ValueError(
                f"Directory {directory} does not appear to contain the gh_pages branch."
            )

    def update_summary(self):
        good_updaters = []
        static_updaters = []
        default_updaters = []
        for updater in updaters:
            if not np.isfinite(updater.update_interval_days):
                static_updaters.append(updater)
            elif (
                updater.authority == "observatory"
                or updater.authority == "converted"
                and updater.updater.authority == "observatory"
            ):
                good_updaters.append(updater)
            elif not np.isfinite(updater.update_interval_days):
                static_updaters.append(updater)
            else:
                default_updaters.append(updater)
        with (self.directory / "status.md").open("wt") as f:
            f.write(
                dedent(
                    """
                    ## Clock correction status

                    This automatically generated file summarizes the status of
                    the clock corrections. It reports the date range covered by
                    the clock corrections as well as when the last attempt was
                    made to update the clock corrections and what happened. The
                    name of each clock file links to a page with more details.

                    """
                )
            )
            self._write_subsection(
                f, "Files with fully automatic updates", good_updaters
            )
            self._write_subsection(f, "Files that should be static", static_updaters)
            self._write_subsection(
                f, "Files that require manual updates", default_updaters
            )
            f.write(
                dedent(
                    """
                    ### Further information:

                    - [What is this repository?](index.html)
                    - [Instructions for using this repository with various software](instructions.html)
                    """
                )
            )

    def _write_subsection(self, f, title, contents):
        f.write("\n\n")
        f.write(f"### {title}\n\n")
        f.write(updater_summary_table(contents, detail_urls=True))

    def generate_details_pages(self):
        for updater in updaters:
            filename = self.directory / f"{updater.filename}.md"
            filename.parent.mkdir(parents=True, exist_ok=True)
            # FIXME: footer?
            filename.write_text(updater.details_page(make_plots_in_dir=self.directory))


updaters.append(
    ClockFileUpdater(
        "GPS to UTC (TEMPO2)",
        "T2runtime/clock/gps2utc_tempo2.clk",
        download_url=tempo2_repository_url.format("gps2utc.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""GPS to UTC clock corrections

            This file is used in the clock correction process for almost all
            observatories.

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.

            In TEMPO2 this file was traditionally generated by a script that parsed
            BIPM Circular T and merged any new data into this file. This has
            resulted in some anomalous entries at the merge points and also
            a change in entries as Circular T has redefined what it publishes
            (early entries in this file are from the column C0, later entries
            are from the column C0').
        """,
    )
)
updaters.append(
    ClockFileCallableUpdater(
        "GPS to UTC",
        "T2runtime/clock/gps2utc.clk",
        authority="observatory",
        callable=bipm.get_gps_merged,
        description="""GPS to UTC clock corrections

            This file is constructed from BIPM published data and should be up-to-date.

            The BIPM publishes two different corrections from GPS to UTC:
            the first, C0, corrects from the GPS Combined Clock to UTC. The second,
            C0', corrects from a timescale that takes advantage of the broadcast
            GPS almanac data to track UTC more closely.

            This file uses C0' data when available, but that is only since 2011.
            Prior to that this uses C0.

            You may want to consider whether your GPS time standard is returning
            the Combined Clock or whether it is using the almanac data. There are
            more specific correction files suitable for one case or the other.

            If you have questions about this, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>. For more detailed questions
            about the BIPM's published corrections, contact <tai@bipm.org>.
        """,
    )
)
updaters.append(
    ClockFileCallableUpdater(
        "GPS to UTC (Combined Clock)",
        "T2runtime/clock/gps2utc_cc.clk",
        authority="observatory",
        callable=bipm.get_gps_c0,
        description="""GPS to UTC clock corrections (Combined Clock)

            This file is constructed from BIPM published data and should be up-to-date.

            The BIPM publishes two different corrections from GPS to UTC:
            the first, C0, corrects from the GPS Combined Clock to UTC. The second,
            C0', corrects from a timescale that takes advantage of the broadcast
            GPS almanac data to track UTC more closely.

            This file uses C0 data, that is, it is for GPS time standards that
            do not take advantage of the almanac data to improve their time
            correction.

            If you have questions about this, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>. For more detailed questions
            about the BIPM's published corrections, contact <tai@bipm.org>.
        """,
    )
)
updaters.append(
    ClockFileCallableUpdater(
        "GPS to UTC (Corrected)",
        "T2runtime/clock/gps2utc_c0p.clk",
        authority="observatory",
        callable=bipm.get_gps_c0p,
        description="""GPS to UTC clock corrections (Corrected)

            This file is constructed from BIPM published data and should be up-to-date.

            The BIPM publishes two different corrections from GPS to UTC:
            the first, C0, corrects from the GPS Combined Clock to UTC. The second,
            C0', corrects from a timescale that takes advantage of the broadcast
            GPS almanac data to track UTC more closely.

            This file uses C0' data, that is, it is for GPS time standards that
            take advantage of the almanac data to improve their time correction.
            Unfortunately the BIPM only publishes these corrections going back
            to 2011.

            If you have questions about this, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>. For more detailed questions
            about the BIPM's published corrections, contact <tai@bipm.org>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "GBT",
        "tempo/clock/time_gbt.dat",
        download_url="https://www.gb.nrao.edu/~fghigo/timer/time_gbt.dat",
        authority="observatory",
        format="tempo",
        obscode="1",
        update_interval_days=1,
        description="""Green Bank Telescope clock correction file

            This file records the difference between UTC(GBT) and UTC(GPS).

            The observatory distributes this file on the Web, updated about daily.

            If questions arise, contact Ryan S. Lynch <rlynch@nrao.edu>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "GBT (TEMPO2)",
        "T2runtime/clock/gbt2gps_tempo2.clk",
        download_url=tempo2_repository_url.format("gbt2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Green Bank Telescope clock corrections (TEMPO2 version)

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileConverterUpdater(
        "GBT (TEMPO2 converted from TEMPO)",
        "T2runtime/clock/gbt2gps.clk",
        format="tempo2",
        description="""Green Bank Telescope clock corrections (TEMPO2 converted version)

            This file is automativally converted from the TEMPO-format GBT
            clock corrections, which are obtained directly from the observatory.
            Thus these can be expected to be fully up to date. Please see the
            GBT clock corrections file entry for further details.

            If questions arise about the original data, contact Ryan S. Lynch
            <rlynch@nrao.edu>.

            If questions arise about the conversion, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>.
        """,
        hdrline="# UTC(GBT) UTC(GPS)",
        updater=get_updater("GBT"),
    )
)

updaters.append(
    ClockFileUpdater(
        "Jodrell Bank (TEMPO)",
        "tempo/clock/time_jb.dat",
        download_url=tempo_repository_url.format("time_jb.dat"),
        authority="temporary",
        format="tempo",
        obscode="8",
        bogus_last_correction=True,
        description="""Jodrell Bank clock correction file

            This file is pulled from the TEMPO repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Jodrell Bank",
        "T2runtime/clock/jb2gps.clk",
        download_url=tempo2_repository_url.format("jb2gps.clk"),
        authority="observatory",
        format="tempo2",
        bogus_last_correction=True,
        description="""Jodrell Bank clock corrections file (TEMPO2)

            Michael Keith periodically generates, manually checks, and updates
            this file in the TEMPO2 repository.

            Note that this contains only corrections for the main site clock;
            data observed with a specific backend (Roach or DFB) also
            need the corrections associated with that backend.

            If questions arise, contact Michael Keith
            <Michael.Keith@manchester.ac.uk>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Jodrell Bank Roach",
        "T2runtime/clock/jbroach2jb.clk",
        download_url=tempo2_repository_url.format("jbroach2jb.clk"),
        authority="observatory",
        format="tempo2",
        bogus_last_correction=True,
        description="""Jodrell Bank Roach backend

            Michael Keith periodically generates, manually checks, and updates
            this file in the TEMPO2 repository.

            Note that this contains corrections for the Roach backend referenced
            to the observatory clock.

            If questions arise, contact Michael Keith
            <Michael.Keith@manchester.ac.uk>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Jodrell Bank DFB",
        "T2runtime/clock/jbdfb2jb.clk",
        download_url=tempo2_repository_url.format("jbdfb2jb.clk"),
        authority="observatory",
        format="tempo2",
        bogus_last_correction=True,
        description="""Jodrell Bank DFB backend

            Michael Keith periodically generates, manually checks, and updates
            this file in the TEMPO2 repository.

            Note that this contains corrections for the DFB backend referenced
            to the observatory clock.

            If questions arise, contact Michael Keith
            <Michael.Keith@manchester.ac.uk>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Arecibo",
        "tempo/clock/time_ao.dat",
        download_url=tempo_repository_url.format("time_ao.dat"),
        authority="temporary",
        format="tempo",
        obscode="3",
        update_interval_days=np.inf,
        invalid_if_older_than=Time("2022-05-20", format="iso"),
        description="""Arecibo clock correction file

            This file covers clock corrections up to the final shut-down before
            the collapse. Any updates are expected to be retroactive
            corrections.

            The earliest clock corrections in this file predate GPS and are
            actually referenced to NIST time directly. Clock corrections from
            after 1995 are referenced to GPS. This file does not distinguish
            between the two.

            If questions arise, contact David Nice <niced@lafayette.edu>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Arecibo (TEMPO2 converted from TEMPO)",
        "T2runtime/clock/ao2gps.clk",
        format="tempo2",
        description="""Arecibo clock corrections (TEMPO2 converted version)

            This file was automativally converted from the TEMPO-format Arecibo
            clock corrections (time_ao.dat), which cover the observatory's full
            operational history. Please see the Arecibo clock corrections for
            details, provenance, and contact information for the original data.

            The earliest clock corrections in time_ao.dat predate GPS and are
            actually referenced to NIST time directly. Clock corrections from
            after 1995 are referenced to GPS. This file has been manually trimmed
            to contain only the GPS-referenced data.

            If questions arise about the original data, contact David Nice
            <niced@lafayette.edu>.

            If questions arise about the conversion, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>.

        """,
        download_url=None,
        invalid_if_older_than=Time("2022-06-07", format="iso"),
        update_interval_days=np.inf,
    )
)

updaters.append(
    ClockFileUpdater(
        "Arecibo (TEMPO2)",
        "T2runtime/clock/ao2gps_tempo2.clk",
        download_url=tempo2_repository_url.format("ao2gps.clk"),
        authority="temporary",
        format="tempo2",
        update_interval_days=np.inf,
        description="""Arecibo clock corrections to GPS (TEMPO2 version)

            The early clock corrections for Arecibo predate GPS and are
            actually referenced directly to NIST. This clock correction file
            separates these out so their corrections can be handled using a
            different clock chain. Unfortunately it does not include
            clock corrections for the last months of operation of Arecibo.

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Arecibo to NIST (TEMPO2)",
        "T2runtime/clock/ao2nist.clk",
        download_url=tempo2_repository_url.format("ao2nist.clk"),
        authority="temporary",
        format="tempo2",
        update_interval_days=np.inf,
        description="""Arecibo clock corrections to UTC(NIST) (TEMPO2 version)

            The early clock corrections for Arecibo predate GPS and are
            actually referenced directly to NIST. This clock correction file
            separates these out so their corrections can be handled using a
            different clock chain.

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "GB140",
        "tempo/clock/time_gb140.dat",
        download_url=tempo_repository_url.format("time_gb140.dat"),
        authority="temporary",
        format="tempo",
        update_interval_days=np.inf,
        description="""Green Bank 140-foot telescope

            This telescope is not currently operating and so updated clock
            corrections should not be necessary. That said, this clock
            correction file is pulled from the TEMPO repository and may not
            cover the entire time that the telescope was operational.

            If questions arise, contact Ryan S. Lynch <rlynch@nrao.edu>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "GB853",
        "tempo/clock/time_gb853.dat",
        download_url=tempo_repository_url.format("time_gb853.dat"),
        authority="temporary",
        format="tempo",
        bogus_last_correction=True,
        update_interval_days=np.inf,
        description="""Green Bank 85-3 telescope

            This is one telescope of a set of three built as a sort of
            prototype interferometer for the VLA. It was operated as a pulsar
            observing instrument for some time after its initial purpose was
            satisfied.

            This telescope is not currently operating and so updated clock
            corrections should not be necessary. That said, this clock
            correction file is pulled from the TEMPO repository and may not
            cover the entire time that the telescope was operational.

            If questions arise, contact Ryan S. Lynch <rlynch@nrao.edu>.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "VLA",
        "tempo/clock/time_vla.dat",
        download_url="https://raw.githubusercontent.com/"
        "nanograv/PINT/master/src/pint/data/runtime/time_vla.dat",
        authority="temporary",
        format="tempo",
        obscode="6",
        description="""Very Large Array clock corrections

            This file is pulled from the PINT repository and may not be fully
            up-to-date. (I think PINT has a more recent version than TEMPO or
            TEMPO2.)
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "VLA (TEMPO2)",
        "T2runtime/clock/vla2gps.clk",
        download_url=tempo2_repository_url.format("vla2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Very Large Array clock corrections (TEMPO2)

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "VLA to NIST",
        "T2runtime/clock/vla2nist.clk",
        download_url=tempo2_repository_url.format("vla2nist.clk"),
        authority="temporary",
        format="tempo2",
        description="""Very Large Array to NIST clock corrections (TEMPO2)

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "FAST",
        "tempo/clock/time_fast.dat",
        download_url="https://raw.githubusercontent.com/"
        "nanograv/PINT/master/src/pint/data/runtime/time_fast.dat",
        authority="temporary",
        format="tempo",
        obscode="k",
        description="""FAST clock correction file

            This file is pulled from the PINT repository and may not be fully
            up-to-date. (TEMPO doesn't seem to have this file at all.)

            The original file is currently hand-generated upon request, but it is
            planned to make the process automatic and the file downloadable (at
            which point we will make it update automatically here).

            If you have any questions about these clock corrections, the person
            to contact is 缪晨晨 <miaocc@bao.ac.cn>, Chenchen Miao.

        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "WSRT",
        "T2runtime/clock/wsrt2gps.clk",
        download_url=tempo2_repository_url.format("wsrt2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Westerbork Synthesis Radio Telescope clock corrections

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "WSRT (TEMPO)",
        "tempo/clock/time_wsrt.dat",
        download_url=tempo_repository_url.format("time_wsrt.dat"),
        authority="temporary",
        format="tempo",
        obscode="i",
        description="""WSRT clock corrections (TEMPO-format)

            This file is pulled from the TEMPO repository and may not be fully
            up-to-date.

            This file may or may not agree with the TEMPO2-format version of what
            should be the same information.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Parkes",
        "T2runtime/clock/pks2gps.clk",
        download_url=tempo2_repository_url.format("pks2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Parkes observatory clock corrections

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.

            The comments read:

                Tie of Parkes clock to GPS time standard. Sources are listed below.
                Where two clock systems existed simultaneously, the dates refer to
                periods when the given clock was supplied as the observatory 1 PPS

                (before this, clock was tied to Tidbinbilla clock: see pks2tid.clk)
                MJD 50844    - 52311.17     Mark IV clock vs Totally Accurate Clock (GPS)
                                              from: update_clkcorr -t pksgps4 gps??.dat
                MJD 52311.17 - now          Mark VI clock vs GPS East
                                              from: update_clkcorr -t pksgps6 pkclk00.*
                -- Russell Edwards 24 September 2004

            The file includes a first entry on MJD 0.00521 with a clock
            correction of 1.04 us; while normally we automatically ignore MJD 0
            for plotting purposes, this value must be in there for a reason so
            we retain it.

        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Parkes (TEMPO)",
        "tempo/clock/time_pks.dat",
        download_url=tempo_repository_url.format("time_pks.dat"),
        authority="temporary",
        format="tempo",
        obscode="7",
        bogus_last_correction=True,
        description="""Parkes observatory clock corrections (TEMPO format)

            This file is pulled from the TEMPO repository and may not be fully
            up-to-date.

            Note that this file has some clock (non-)correction data for other
            telescopes in the same file, distinguished only by observatory code.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "SRT",
        "T2runtime/clock/srt2gps.clk",
        download_url=tempo2_repository_url.format("srt2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Sardinia Radio Telescope clock corrections

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Effelsberg",
        "T2runtime/clock/eff2gps.clk",
        download_url=tempo2_repository_url.format("eff2gps.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""Effelsberg telescope clock corrections

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.

            Originally made from time_bonn.dat with an awk script, according to
            the comments.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Effelsberg Asterix/PSRix",
        "T2runtime/clock/effix2gps.clk",
        download_url=tempo2_repository_url.format("effix2gps.clk"),
        authority="temporary",
        format="tempo2",
        description="""Effelsberg Asterix/PSRix clock correction file

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date. The European Pulsar Timing Array maintains an internal
            repository of clock corrections, which they have transferred to the TEMPO2
            repository, so  EPTA telescope data in the TEMPO2 repository (and
            thus here) can be expected to be somewhat up to date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "LEAP",
        "T2runtime/clock/leap2effix.clk",
        download_url=tempo2_repository_url.format("leap2effix.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""LEAP clock correction file

            This file corrects from the LEAP clock to the Effelsberg Asterix
            clock; then the effix2gps file can be used to convert to GPS.

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date. The European Pulsar Timing Array maintains an internal
            repository of clock corrections, which they have transferred to the TEMPO2
            repository, so  EPTA telescope data in the TEMPO2 repository (and
            thus here) can be expected to be somewhat up to date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "NUPPI",
        "tempo/clock/time_nuppi.dat",
        download_url=tempo_repository_url.format("time_nuppi.dat"),
        authority="temporary",
        format="tempo",
        description="""Clock corrections specifically for the NUPPI backend at Nancay

            This file is pulled from the TEMPO repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Meerkat (observatory)",
        "T2runtime/clock/mk2utc_observatory.clk",
        download_url="https://archive-gw-1.kat.ac.za/public/tfr/mk2utc.clk",
        authority="observatory",
        format="tempo2",
        bogus_last_correction=False,
        description="""MeerKAT clock corrections file

            This file is distributed by the observatory. It records the local
            clock difference from (I think) GPS. It may cause some problems
            for TEMPO2 as it has a header line "# UTC(MK) UTC" when TEMPO2
            would expect "# UTC(meerkat) UTC" or "# UTC(meerkat) UTC(GPS)".

            If questions arise, contact Ryan Shannon <rshannon@swin.edu.au>
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Meerkat (TEMPO2)",
        "T2runtime/clock/mk2utc.clk",
        download_url=tempo2_repository_url.format("mk2utc.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""MeerKAT clock corrections file (TEMPO2)

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "MOST",
        "T2runtime/clock/mo2gps.clk",
        download_url=tempo2_repository_url.format("mo2gps.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""\
            Molonglo Observatory Synthesis Telescope clock corrections file (TEMPO2)

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "Nancay to obspm",
        "T2runtime/clock/ncyobs2obspm.clk",
        download_url=tempo2_repository_url.format("ncyobs2obspm.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""Nancay-related clock corrections?

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.

            The European Pulsar Timing Array maintains an internal repository
            of clock corrections, which they have transferred to the TEMPO2
            repository, so  EPTA telescope data in the TEMPO2 repository (and
            thus here) can be expected to be somewhat up to date.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "CHIME",
        "T2runtime/clock/chime2gps.clk",
        authority="observatory",
        format="tempo2",
        bogus_last_correction=True,
        update_interval_days=np.inf,
        description="""CHIME (null) clock corrections

            CHIME records data directly against GPS time, and thus no clock
            corrections are necessary. This file is a placeholder to make that
            obvious.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "GMRT",
        "T2runtime/clock/gmrt2gps.clk",
        authority="observatory",
        format="tempo2",
        bogus_last_correction=True,
        update_interval_days=np.inf,
        description="""GMRT (null) clock corrections

            The GMRT records data directly against GPS time, and thus no clock
            corrections are necessary. This file is a placeholder to make that
            obvious.
        """,
    )
)
updaters.append(
    ClockFileUpdater(
        "obspm",
        "T2runtime/clock/obspm2gps.clk",
        download_url=tempo2_repository_url.format("obspm2gps.clk"),
        authority="temporary",
        format="tempo2",
        bogus_last_correction=True,
        description="""Nancay-related clock corrections?

            This file is pulled from the TEMPO2 repository and may not be fully
            up-to-date.

            The European Pulsar Timing Array maintains an internal repository
            of clock corrections, which they have transferred to the TEMPO2
            repository, so  EPTA telescope data in the TEMPO2 repository (and
            thus here) can be expected to be somewhat up to date.
        """,
    )
)
updaters.append(
    CallableUpdater(
        "Leap seconds",
        "tempo/clock/leap.sec",
        callable=iers.make_leap_sec,
        authority="observatory",
        description="""Leap seconds table

            This file lists the MJDs of leap seconds, starting from 41499.
            The format can only accommodate positive leap seconds (but all
            leap seconds so far have been positive).

            This file is generated from Astropy's parsing of the IERS
            bulletins. It should be updated at least six months in advance
            of any planned leap second (and not otherwise).

            If there are any questions, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>.
        """,
    )
)
updaters.append(
    CallableUpdater(
        "UT1 table",
        "tempo/clock/ut1.dat",
        callable=iers.make_ut1_dat,
        authority="observatory",
        description="""UT1 table

            This file records the Earth's actual rotation in the form of
            corrections TAI-UT1 in a format readable by TEMPO.

            This file is generated from Astropy's parsing of the IERS
            bulletins. It should be updated approximately monthly, and it
            includes the IERS predictions covering about a year after the
            publication date.

            This differs slightly from the version traditionally distributed
            with TEMPO - that is generated by a combination of a perl script
            parsing the output from the IERS web form and a custom C program
            generating predictions. As a result, this generated file may not
            extend as far into the future as the conventional ut1.dat does.
            There are also minor differences in some of the early values; the
            origin of these early values is not completely clear, and some of
            them predate the earliest values in the IERS bulletins Astropy uses.

            If there are any questions, contact Anne Archibald
            <anne.archibald@newcastle.ac.uk>.
        """,
    )
)
for y in bipm.list_recent_ttbipmxy()[::-1]:
    updaters.append(
        ClockFileCallableUpdater(
            f"TAI to TT(BIPM{y})",
            f"T2runtime/clock/tai2tt_bipm{y}.clk",
            authority="observatory",
            callable=lambda: bipm.get_ttbipmxy_corrections_clock(
                y, include_forecast=1000
            ),
            update_interval_days=np.inf,
            description=f"""TAI to BIPM-updated TT, {y} version

                This file is constructed from BIPM published data and should
                never change; updated versions will appear approximately
                yearly, and do revise old data. Aa result they are given different
                clock file names, and are treated as different time scales.

                The time scale TT is supposed to be a basis for TDB, and is meant
                to be a stable clock for describing the motions of the solar system.
                Of necessity it is derived from the practical time scale TAI,
                which is produced by an ensemble of atomic clocks. A simple
                realization of TT, such as that implemented by Astropy,
                simply yields TT = TAI + 32.184 s.

                Atomic clocks do wander, and the BIPM can sometimes estimate
                that wander in retrospect.  Rather than revise TAI, the BIPM
                offers versions of TT that are more stable because they
                compensate for variations in TAI. These are defined by yearly
                bulletins, and are referred to in TEMPO2 as TT(BIPMyyyy), where
                yyyy is the year of the bulletin.

                Each bulletin publishes corrections from TAI to TT. It may
                revise earlier corrections up to about 10 years back, and it
                contains a formula for making predictions past the end of the
                data it contains.

                This clock file is automatically generated from the bulletin
                for {y}. It contains forecasted values for 1000 days past the
                end of the tabulated data. This is marked by a comment in the
                clock file itself.

                If you have questions about this, contact Anne Archibald
                <anne.archibald@newcastle.ac.uk>. For more detailed questions
                about the BIPM's published corrections, contact <tai@bipm.org>.
            """,
        )
    )
for y in [
    2019,
    2018,
    2017,
    2016,
    2015,
    2014,
    2013,
    2012,
    2011,
    2010,
    "06",
    "05",
    2004,
    2003,
    "01",
    92,
]:
    updaters.append(
        ClockFileUpdater(
            f"TAI to TT(BIPM{y})",
            f"T2runtime/clock/tai2tt_bipm{y}.clk",
            download_url=tempo2_repository_url.format(f"tai2tt_bipm{y}.clk"),
            authority="temporary",
            format="tempo2",
            update_interval_days=np.inf,
            bogus_last_correction=True,
            description=f"""TAI to BIPM-updated TT, {y} version

                This file is constructed from BIPM published data and should
                never change; updated versions will appear approximately
                yearly, and do revise old data. Aa result they are given different
                clock file names, and are treated as different time scales.

                The time scale TT is supposed to be a basis for TDB, and is meant
                to be a stable clock for describing the motions of the solar system.
                Of necessity it is derived from the practical time scale TAI,
                which is produced by an ensemble of atomic clocks. A simple
                realization of TT, such as that implemented by Astropy,
                simply yields TT = TAI + 32.184 s.

                Atomic clocks do wander, and the BIPM can sometimes estimate
                that wander in retrospect.  Rather than revise TAI, the BIPM
                offers versions of TT that are more stable because they
                compensate for variations in TAI. These are defined by yearly
                bulletins, and are referred to in TEMPO2 as TT(BIPMyyyy), where
                yyyy is the year of the bulletin.

                Each bulletin publishes corrections from TAI to TT. It may
                revise earlier corrections up to about 10 years back, and it
                contains a formula for making predictions past the end of the
                data it contains.

                This file is pulled from the TEMPO2 repository but is based on
                BIPM data and should be unchanging.
            """,
        )
    )
