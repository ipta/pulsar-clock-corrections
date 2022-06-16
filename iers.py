from io import StringIO

import astropy.units as u
import astropy.utils.iers
import numpy as np
from astropy.time import Time

def get_leap_sec():
    ls = astropy.utils.iers.LeapSeconds.auto_open()
    # Annoyingly it's year/month/amount
    # Annoyingly tempo's leap.sec starts later than integer leap seconds
    leap_sec = []
    leap_sec_values = []
    for r in ls:
        t = Time(f"{r['year']}-{r['month']}-01", format="iso", scale="utc")
        leap_sec.append(int(np.round(t.mjd)))
        leap_sec_values.append(r["tai_utc"])

    return np.array(leap_sec), np.array(leap_sec_values)

def make_leap_sec():
    """Construct leap.sec file."""
    leap_sec, leap_sec_values = get_leap_sec()

    tstart = np.inf
    tend = -np.inf

    r = StringIO()
    for i, m in enumerate(leap_sec):
        if m < 41499:
            # not in leap.sec
            continue
        tstart = min(tstart, m)
        tend = max(tend, m)
        print(m, file=r)
        if len(leap_sec_values) > 1 and leap_sec_values[i] <= leap_sec_values[i-1]:
            # This is a problem for TEMPO
            raise ValueError(f"Leap seconds not all positive: {ls}")
    return r.getvalue(), Time(tstart, format="mjd"), Time(tend, format="mjd")

def make_ut1_dat():
    r = StringIO()
    leap_sec, leap_sec_values = get_leap_sec()
    iers_a = astropy.utils.iers.IERS_Auto.open()
    tai_utc = np.array(leap_sec_values)[np.searchsorted(leap_sec, iers_a["MJD"],side="right")-1]*u.s
    print("""\
    TAI-UT1: IERS A/B via Astropy including forecast for about a year
    (A3,2X,I5,6(I7,1X),1X,I2)        2                  6  5           1.E-4""", file=r)
    ut1_utc = iers_a["UT1_UTC"]
    tai_ut1 = tai_utc - ut1_utc
    i = 0
    while i<len(iers_a):
        mjd = int(iers_a[i]["MJD"].to_value(u.d))
        ut1mutcs = [tai_ut1[i+5*j] for j in range(6) if i+5*j<len(iers_a)]
        e = f"     {mjd:5d}"
        e += "".join([f"{int(np.round(uv.to_value(u.us)/100)):7d} " for uv in ut1mutcs])
        if len(ut1mutcs)<6:
            e += (8*" ")*(6-len(ut1mutcs))+f" {len(ut1mutcs):2d}"
        print(e, file=r)
        i += 30
    print("END", file=r)

    return r.getvalue(), Time(iers_a[0]["MJD"], format="mjd"), Time(iers_a[-1]["MJD"], format="mjd")
