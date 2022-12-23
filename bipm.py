"""Tools for downloading and parsing BIPM data.

BIPM Circular T records the differences between UTC inferred from GPS and
actual GPS. It has changed format and content a number of times, and it has had
errata published, but the issued Circular T values do not change. As a result
it can make sense to use updated summary tables published by the BIPM. There
are also two different ways to infer UTC from GPS, and the BIPM has published
two different versions (C0 and C0').

"""
import re
from io import StringIO
from textwrap import dedent

import numpy as np
import astropy.utils.data
import astropy.units as u
from astropy.time import Time

import pint.observatory.clock_file

# The actual Circular T bulletins
circular_t_url = "https://webtai.bipm.org/ftp/pub/tai/Circular-T/cirt/cirt.{}"
heading_re = re.compile(r"^ *\d+ - \S.*$")

# A summary file containing C0 and C0' as well as corrected errata, from 2011 to recently
# Is this updated regularly? Maybe when each Circular T is released? Last MJD 59699, same
# as current last Circular T.
utcgnss_url = "https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss"

# Yearly tables 1993 to 2003 containing C0
utcgps_old = "ftp://ftp2.bipm.org/pub/tai/scale/UTCGPS/utcgps{}.ar"

# Yearly tables 2003 to 2015 containing C0 and, for 2011 on, C0'
utcgps_med = "ftp://ftp2.bipm.org/pub/tai/scale/UTCGPSGLO/utcgpsglo{}.ar"

# Explanatory supplement
# https://webtai.bipm.org/ftp/pub/tai/other-products/notes/explanatory_supplement_v0.6.pdf

# Parsing guide for Circular T (not necessarily old ones)
# https://webtai.bipm.org/ftp/pub/tai/other-products/notes/cirt_format_v0.1.txt
# https://webtai.bipm.org/ftp/pub/tai/other-products/notes/cirt_format_v0.2.txt


def read_recent_gps_corrections():
    """Read the table of 2011-now GPS to UTC corrections.

    This will download a new version if the old appears to be out of date.

    Returns
    -------
    np.ndarray
        The shape will be n by 3, with the columns MJD, C0, C0'; the last two
        are in nanoseconds.
    """
    cols = (0, 1, 4)
    r = np.loadtxt(
        astropy.utils.data.download_file(utcgnss_url, cache=True), usecols=cols
    )
    # The Circular T covering April was released May 12
    permitted_age = 31 + 12
    if Time.now().mjd - r[-1, 0] > permitted_age:
        r = np.loadtxt(
            astropy.utils.data.download_file(utcgnss_url, cache=True), usecols=cols
        )
    return r


def read_old_gps_corrections():
    """Read pre-2011 GPS to UTC corrections.

    This contains only the value C0 as that is all the BIPM pubished.

    Returns
    -------
    np.ndarray
        The shape will be n by 2, with the columns MJD, C0. C0 is in nanoseconds.
    """
    mjds = []
    c0s = []
    for year in range(1993, 2004):
        # print(f"reading old year {year}")
        yy = str(year)[-2:]
        with open(
            astropy.utils.data.download_file(utcgps_old.format(yy), cache=True),
            encoding="latin-1",
        ) as f:
            n_found = 0
            for line in f:
                ls = line.split()
                if len(ls) != 6:
                    continue
                try:
                    mjd = int(ls[2])
                except ValueError:
                    continue
                if not 40000 < mjd < 60000:
                    continue
                if mjds and mjd < mjds[-1]:
                    # print(f"MJD {mjd} less than last previous mjd: {mjds[-10:]}")
                    continue
                try:
                    c0 = float(ls[3])
                except ValueError:
                    continue
                mjds.append(mjd)
                c0s.append(c0)
                n_found += 1
            if n_found == 0:
                raise ValueError(f"No data found in year {year}")
    for year in range(2003, 2011):
        # print(f"reading medium year {year}")
        yy = str(year)[-2:]
        with open(
            astropy.utils.data.download_file(utcgps_med.format(yy), cache=True),
            encoding="latin-1",
        ) as f:
            n_found = 0
            for line in f:
                ls = line.split()
                if len(ls) != 7:
                    continue
                try:
                    mjd = int(ls[2])
                except ValueError:
                    continue
                if not 40000 < mjd < 60000:
                    continue
                try:
                    c0 = float(ls[3])
                except ValueError:
                    continue
                if mjds and mjd < mjds[-1]:
                    # print(f"MJD {mjd} less than last previous mjd: {mjds[-10:]}")
                    continue
                mjds.append(mjd)
                c0s.append(c0)
                n_found += 1
            if n_found == 0:
                raise ValueError(f"No data found in year {year}")

    return np.array([mjds, c0s]).T


def get_gps_c0():
    """Obtain BIPM measurements of GPS CC to UTC correction as a ClockFile."""
    a = read_old_gps_corrections()
    b = read_recent_gps_corrections()
    if a[-1, 0] > b[0, 0]:
        raise ValueError(f"MJDs overlap: {a[-10:]} vs {b[:10]}")
    mjds = np.concatenate([a[:, 0], b[:, 0]])
    c0s = np.concatenate([a[:, 1], b[:, 1]])
    hdrline = "# UTC(GPS)_CC UTC(USNO)"
    leading_comment = dedent(
        """\
        # Corrections from UTC inferred from the GPS Combined Clock to UTC.
        # Leap seconds do not appear here, and the Combined Clock is steered
        # to try to make it approximate UTC, but there is some residual drift.
        #
        # Note that the GPS "almanac" signal also includes predictions of its
        # deviations from UTC, so the Combined Clock is not necessarily the best
        # available approximation of UTC; a suitable receiver can do better.
        #
        # The BIPM publishes these values as "C0", from about 1995 to the present.
        # The BIPM also publishes corrections for the predicted UTC, but only from
        # 2011. Those are available in a separate file.
        #
        # The first values in this file are from the BIPM yearly summary tables
        # available for years YY=93 to 03 from
        # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPS/utcgpsYY.ar
        # and for years YY=03 to 11 from
        # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPSGLO/utcgpsgloYY.ar
        # Later entries in the file (there is a comment to mark the place)
        # are obtained from
        # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss
        # which is updated monthly.
        #
    """
    )
    comments = [""] * len(c0s)
    comments[
        len(a) - 1
    ] = "\n# These entries are from https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss"
    c = pint.observatory.clock_file.ClockFile(
        mjd=mjds,
        clock=c0s * u.ns,
        comments=comments,
        filename="gps_cc2utc.clk",
    )
    c.leading_comment = leading_comment
    c.header = hdrline
    return c


def get_gps_c0p():
    """Obtain BIPM measurements of GPS USNO forecasts to UTC correction as a ClockFile."""
    a = read_recent_gps_corrections()
    mjds = a[:, 0]
    c0ps = a[:, 2]
    hdrline = "# UTC(GPS)_C0P UTC(USNO)"
    leading_comment = dedent(
        """\
        # Corrections from the GPS predictions of UTC to UTC.
        # Leap seconds do not appear here.
        #
        # Note that the GPS "almanac" signal also includes predictions of the
        # Combined Clock's deviations from UTC, so a suitable receiver can produce a
        # good approximation of UTC. This file records the errors in that approximation.
        #
        # The BIPM publishes these values as "C0'", from about 2011 to the present.
        # The BIPM also publishes corrections for the Combined Clock, going back to
        # 1993. Those are available in a separate file.
        #
        # The data in this file is obtained from
        # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss
        # which is updated monthly.
        #
    """
    )
    comments = [""] * len(c0ps)
    c = pint.observatory.clock_file.ClockFile(
        mjd=mjds,
        clock=c0ps * u.ns,
        comments=comments,
        filename="gps_c0p2utc.clk",
    )
    c.leading_comment = leading_comment
    c.header = hdrline
    return c


def get_gps_merged():
    """Obtain a best-effort clock correction as a ClockFile.

    This is based on C0' when available and C0 when C0' is not.
    """
    a = read_old_gps_corrections()
    b = read_recent_gps_corrections()
    if a[-1, 0] > b[0, 0]:
        raise ValueError(f"MJDs overlap: {a[-10:]} vs {b[:10]}")
    mjds = np.concatenate([a[:, 0], b[:, 0]])
    c0s = np.concatenate([a[:, 1], b[:, 2]])
    hdrline = "# UTC(GPS) UTC(USNO)"
    leading_comment = dedent(
        """\
        # Corrections from GPS to UTC.
        # Leap seconds do not appear here.
        #
        # Note that the GPS "almanac" signal also includes predictions of the
        # Combined Clock's deviations from UTC, so a suitable receiver can produce a
        # good approximation of UTC.
        #
        # The BIPM publishes these values as "C0'", from about 2011 to the present.
        # The BIPM also publishes corrections for the Combined Clock, going back to
        # 1993. This file contains both: when available, we use C0', before that we
        # use C0. This may or may not resemble what your GPS receiver system uses.
        #
        # The first values in this file are from the BIPM yearly summary tables
        # available for years YY=93 to 03 from
        # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPS/utcgpsYY.ar
        # and for years YY=03 to 11 from
        # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPSGLO/utcgpsgloYY.ar
        # Later entries in the file (there is a comment to mark the place)
        # are obtained from
        # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss
        # which is updated monthly.
        #
        # These entries are based on C0 values.
    """
    )
    comments = [""] * len(c0s)
    comments[
        len(a) - 1
    ] = "\n# These entries are from https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss\n# These entries are based on C0' values."
    c = pint.observatory.clock_file.ClockFile(
        mjd=mjds,
        clock=c0s * u.ns,
        comments=comments,
        filename="gps2utc.clk",
    )
    c.leading_comment = leading_comment
    c.header = hdrline
    return c


ttbipmxy_url = "https://webtai.bipm.org/ftp/pub/tai/ttbipm/TTBIPM.{}"


def list_recent_ttbipmxy():
    # Start from the first year not in the TEMPO2 repository
    year = 2020

    years = []
    while True:
        try:
            f = astropy.utils.data.download_file(ttbipmxy_url.format(year), cache=True)
        except IOError:
            break
        else:
            years.append(year)
            year += 1
    return years


prediction_re = re.compile(
    r"^TT\(BIPM..\) = TAI \+ (\d+\.\d+) s \+ (\d+\.\d+) ns ([-+]) (\d+\.\d+)x\(MJD-(\d+)\) ns\s*$"
)
column_re = re.compile(
    r'^ +3rd +" +: TT.BIPM... - TAI - (\d+\.\d+) s, unit is one microsecond\s*$'
)


def get_ttbipmxy_corrections(year, include_forecast=1000):
    """Get the TAI to TT corrections from the BIPM"""
    # FIXME: which way do these corrections go? The BIPM is clear but what
    # does TEMPO2 want? PINT?
    with open(
        astropy.utils.data.download_file(ttbipmxy_url.format(year), cache=True)
    ) as f:
        leading_comment_io = StringIO()
        for line in f:
            leading_comment_io.write("# ")
            leading_comment_io.write(line)
            if m := prediction_re.match(line):
                prediction_offset_s = float(m.group(1))
                prediction_offset_ns = float(m.group(2))
                prediction_rate_ns_per_day = float(m.group(3) + m.group(4))
                prediction_base_mjd = float(m.group(5))
                break
        else:
            raise ValueError("Prediction line not recognized")
        for line in f:
            leading_comment_io.write("# ")
            leading_comment_io.write(line)
            if m := column_re.match(line):
                tai_offset = float(m.group(1))
                break
        else:
            raise ValueError("Column definition not recognized")
        data = np.loadtxt(f)
    mjds = data[:, 0]
    values_us = data[:, 2]
    corr_s = tai_offset + values_us * 1e-6

    extra_mjds = mjds[-1] + np.arange(1, include_forecast + 1)
    extra_corr_s = (
        prediction_offset_s
        + (
            prediction_offset_ns
            + prediction_rate_ns_per_day * (extra_mjds - prediction_base_mjd)
        )
        * 1e-9
    )

    return leading_comment_io.getvalue(), mjds, corr_s, extra_mjds, extra_corr_s


def get_ttbipmxy_corrections_clock(year, include_forecast=1000):
    leading_comment, mjds, corr_s, extra_mjds, extra_corr_s = get_ttbipmxy_corrections(
        year, include_forecast=include_forecast
    )
    all_mjds = np.concatenate([mjds, extra_mjds])
    all_corr_s = np.concatenate([corr_s, extra_corr_s])
    comments = [""] * len(all_mjds)
    comments[len(mjds) - 1] = "\n# Extrapolation starts here"
    c = pint.observatory.clock_file.ClockFile(
        mjd=all_mjds,
        clock=all_corr_s * u.s,
        comments=comments,
        filename=f"tai2tt_bipm{year}.clk",
    )
    c.leading_comment = leading_comment
    c.header = "# TAI TT(BIPM2019)"
    return c
