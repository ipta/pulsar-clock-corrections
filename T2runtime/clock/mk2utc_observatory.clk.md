
## Meerkat (observatory)

MeerKAT clock corrections file

This file is distributed by the observatory. It records the local
clock difference from (I think) GPS. It may cause some problems
for TEMPO2 as it has a header line "# UTC(MK) UTC" when TEMPO2
would expect "# UTC(meerkat) UTC" or "# UTC(meerkat) UTC(GPS)".

If questions arise, contact Ryan Shannon <rshannon@swin.edu.au>

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/mk2utc_observatory.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/mk2utc_observatory.clk> |
| Original download URL | <https://archive-gw-1.kat.ac.za/public/tfr/mk2utc.clk> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 2019-01-01 MJD 58484.0 |
| Clock file end | 2026-03-11 MJD 61111.0 |
| Update interval (days) | 7 |
| Last update attempt | 2026-04-10 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2026-01-26 20:50:01.083 - Unchanged
2026-02-03 21:02:20.809 - Unchanged
2026-02-10 21:08:08.520 - Unchanged
2026-02-17 21:03:24.266 - Updated
2026-03-06 20:56:20.131 - Updated
2026-03-13 21:00:06.998 - Unchanged
2026-03-20 20:57:53.594 - Updated
2026-03-27 21:04:43.296 - Unchanged
2026-04-03 21:02:14.300 - Unchanged
2026-04-10 21:03:02.691 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1773735946.550529 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

