
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
| Clock file end | 2026-04-10 MJD 61141.0 |
| Update interval (days) | 7 |
| Last update attempt | 2026-06-26 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2026-04-24 21:13:55.408 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-05-01 21:14:58.443 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-05-08 21:35:06.285 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-05-15 21:35:46.293 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-05-22 21:43:27.333 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-05-29 22:14:17.427 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-06-05 21:54:17.072 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-06-12 22:06:24.887 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-06-19 21:43:02.632 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
2026-06-26 21:48:41.646 - Validation failed: New version of T2runtime/clock/mk2utc_observatory.clk MJDs differ from old version where they overlap in 7 places
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1776326930.598292 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

