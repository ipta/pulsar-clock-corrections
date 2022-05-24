import inspect
import os
import re
from io import StringIO
from pathlib import Path
from textwrap import dedent

import numpy as np
from astropy.time import Time
from astropy.utils.data import download_file
from pint.observatory.clock_file import ClockFile

public_repo_url_raw = (
    "https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/"
)


def base_location():
    return Path(__file__).parent


def list_candidate_clock_files():
    return sorted(base_location().glob("tempo/clock/time*_*.dat")) + sorted(
        base_location().glob("T2runtime/clock/*2*.clk")
    )


class ValidationError(RuntimeError):
    pass


class ClockFileUpdater:
    def __init__(
        self,
        short_description,
        filename,
        authority="temporary",
        download_url=None,
        format="tempo",
        bogus_last_entry=False,
        obscode=None,
        invalidate_if_older_than=None,
        update_interval_days=7,
        description="",
    ):
        self.filename = filename
        self.short_description = short_description
        self.filepath = base_location() / self.filename
        self.authority = authority
        self.format = format
        self.bogus_last_entry = bogus_last_entry
        self.download_url = download_url
        self.obscode = obscode
        self.invalidate_if_older_than = invalidate_if_older_than
        self.update_interval_days = update_interval_days
        self.description = inspect.cleandoc(description)
        self._last_log_entry = None
        self.log_entry_re = re.compile(r"([0-9 :.-]+) - ([^:]+)(: (.*))?")
        self._clock_file = None

    @property
    def log_file(self):
        return base_location() / "log" / (self.filename + ".log")

    def add_to_log(self, msg):
        entry = Time.now().iso + " - " + msg + "\n"
        with open(self.log_file, "at") as f:
            f.write(entry)
        self._last_log_entry = entry

    @property
    def last_log_entry(self):
        if self._last_log_entry is None:
            self._last_log_entry = open(self.log_file, "rt").readlines()[-1]
        return self._last_log_entry

    def parse_log_entry(self, entry):
        r = self.log_entry_re.match(entry.strip())
        reason = r.group(4)
        if reason is None:
            reason = ""
        return Time(r.group(1), format="iso"), r.group(2), reason

    def get(self, cache=False):
        return download_file(self.download_url, cache=cache)

    @property
    def clock_file(self):
        if self._clock_file is None:
            self._clock_file = ClockFile.read(
                base_location() / self.filename,
                format=self.format,
                bogus_last_entry=self.bogus_last_entry,
                obscode=self.obscode,
            )
        return self._clock_file

    def validate(self, new_file):
        old = self.clock_file
        new = ClockFile.read(
            new_file,
            format=self.format,
            bogus_last_entry=self.bogus_last_entry,
            obscode=self.obscode,
        )
        if len(old.time) > len(new.time):
            raise ValidationError(
                f"New version of {self.filename} has decreased from {len(old.clock)} to {len(new.clock)} measurements."
            )
        d = old.time != new.time[: len(old.time)]
        if np.any(d):
            raise ValidationError(
                f"New version of {self.filename} MJDs differ from old version where they overlap in {np.sum(d)} places"
            )
        d = old.clock != new.clock[: len(old.clock)]
        if np.any(d):
            raise ValidationError(
                f"New version of {self.filename} clock corrections differ from old version where they overlap in {np.sum(d)} places"
            )

    def try_update(self, cache=False):
        try:
            f = self.get(cache=cache)
        except IOError as e:
            self.add_to_log(f"Failed to download: {e}")
            return False
        old_contents = self.filepath.read_text()
        new_contents = Path(f).read_text()
        if old_contents == new_contents:
            self.add_to_log(f"Unchanged")
            return True
        try:
            self.validate(f)
        except ValidationError as e:
            self.add_to_log(f"Validation failed: {e}")
            return False
        self.filepath.write_text(new_contents)
        self._clock_file = None
        self.add_to_log(f"Updated")
        return True

    def details_page(self):
        tstart = self.clock_file.time[0]
        tend = self.clock_file.time[-2 if self.bogus_last_entry else -1]
        last_date, result, details = self.parse_log_entry(self.last_log_entry)
        log_url = public_repo_url_raw + "log/" + self.filename + ".log"
        f = StringIO()
        f.write(
            dedent(
                f"""
            {self.short_description}
            ---------------------------
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
            | Download URL | <{self.download_url}> |
            | Format | {self.format} |
            | Bogus last entry | {self.bogus_last_entry} |
            | Clock file start | {short_date(tstart)} MJD {tstart.mjd:.1f} |
            | Clock file end | {short_date(tend)} MJD {tend.mjd:.1f} |
            | Update interval (days) | {self.update_interval_days} |
            | Last update attempt | {short_date(last_date)} |
            | Last update result | {result} |

            Log entries from the last few update attempts:
            """
            )
        )
        f.write("```\n")
        for l in self.log_file.open().readlines()[-10:]:
            f.write(l)
        f.write("```\n")
        f.write(f"[Full log]({log_url})\n")
        return f.getvalue()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.short_description!r}, {self.filename!r})"
        )


tempo_repository_url = "https://raw.githubusercontent.com/nanograv/tempo/master/clock/"

updaters = [
    ClockFileUpdater(
        "GBT",
        "tempo/clock/time3_gbt.dat",
        download_url="https://www.gb.nrao.edu/~fghigo/timer/time_gbt.dat",
        authority="observatory",
        format="tempo",
        obscode="1",
        update_interval_days=1,
        description="""GBT clock correction file

            The observatory distributes this file on the Web, updated about daily.

            If questions arise, contact ???
        """,
    ),
    ClockFileUpdater(
        "Jodrell Bank",
        "tempo/clock/time_jb.dat",
        download_url=tempo_repository_url + "time_jb.dat",
        authority="temporary",
        format="tempo",
        obscode="8",
        bogus_last_entry=True,
        description="""Jodrell Bank clock correction file

            This file is pulled from the TEMPO repository and may not be fully up-to-date.
        """,
    ),
    ClockFileUpdater(
        "Arecibo",
        "tempo/clock/time_ao.dat",
        download_url=tempo_repository_url + "time_ao.dat",
        authority="temporary",
        format="tempo",
        obscode="3",
        update_interval_days=np.inf,
        description="""Arecibo clock correction file

            Since the telescope collapse, this file should not need additional updates.
        """,
    ),
    ClockFileUpdater(
        "FAST",
        "tempo/clock/time_fast.dat",
        download_url="https://raw.githubusercontent.com/nanograv/PINT/master/src/pint/data/runtime/time_fast.dat",
        authority="temporary",
        format="tempo",
        obscode="k",
        bogus_last_entry=True,
        description="""FAST clock correction file

            This file is pulled from the PINT repository and may not be fully up-to-date.
        """,
    ),
]


def get_updater(name):
    for u in updaters:
        if (
            u.short_description.lower() == name.lower()
            or u.filename == name
            or Path(u.filename).name == name
        ):
            return u
    else:
        raise ValueError(f"Unable to find an updater for {name}")


def try_all_updates():
    for u in updaters:
        u.try_update()


def short_date(t):
    return t.datetime.strftime("%Y-%m-%d")


def updater_summary_table(detail_urls=False):
    o = StringIO()
    print(
        f"| Name "
        f"| File "
        f"| Corrections start "
        f"| Corrections end "
        f"| Last check date "
        f"| Last check result ",
        file=o,
    )
    print(f"|:--- |:--- | --- | --- | --- |:--- ", file=o)
    for u in updaters:
        tstart = u.clock_file.time[0]
        tend = u.clock_file.time[-2 if u.bogus_last_entry else -1]
        last_date, result, details = u.parse_log_entry(u.last_log_entry)
        if result not in {"Unchanged", "Updated"}:
            result = "**" + result + "**"
        detail_url = u.filename + ".html"
        if detail_urls:
            print(
                f"| [{u.short_description}]({detail_url}) "
                f"| `{u.filename}` "
                f"| {short_date(tstart)} MJD {tstart.mjd:.1f} "
                f"| {short_date(tend)} MJD {tend.mjd:.1f} "
                f"| {short_date(last_date)} "
                f"| {result} ",
                file=o,
            )
        else:
            print(
                f"| {u.short_description} "
                f"| `{u.filename}` "
                f"| {short_date(tstart)} MJD {tstart.mjd:.1f} "
                f"| {short_date(tend)} MJD {tend.mjd:.1f} "
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

    def __init__(self, directory):
        self.directory = Path(directory)
        if not (self.directory / ".this_is_gh_pages").exists():
            raise ValueError(
                f"Directory {directory} does not appear to contain the gh_pages branch."
            )

    def update_summary(self):
        with (self.directory / "status.md").open("wt") as f:
            f.write(
                dedent(
                    """
                Clock correction status
                -----------------------

                This automatically generated file summarizes the status of the clock
                corrections. It reports the date range covered by the clock corrections
                as well as when the last attempt was made to update the clock corrections
                and what happened. The name of each clock file links to a page with more
                details.

                """
                )
            )
            f.write("\n\n")
            f.write(updater_summary_table(detail_urls=True))
            f.write("\n\n")
            f.write(
                dedent(
                    """
                Further information:

                - [What is this repository?](index.html)
                - [Instructions for using this repository with various software](instructions.html)
                """
                )
            )

    def generate_details_pages(self):
        for updater in updaters:
            filename = self.directory / (updater.filename + ".md")
            filename.parent.mkdir(parents=True, exist_ok=True)
            # FIXME: footer? plots?
            filename.write_text(updater.details_page())
