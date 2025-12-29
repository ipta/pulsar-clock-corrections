
## Meerkat (TEMPO2)

MeerKAT clock corrections file (TEMPO2)

This file is pulled from the TEMPO2 repository and may not be fully
up-to-date.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/mk2utc.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/mk2utc.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/mk2utc.clk> |
| Format | tempo2 |
| Bogus last correction | True |
| Clock file start | 2019-01-01 MJD 58484.0 |
| Clock file end | 2024-09-23 MJD 60576.9 |
| Update interval (days) | 7 |
| Last update attempt | 2025-12-29 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2025-10-27 20:40:10.855 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-11-03 20:43:01.067 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-11-10 20:44:59.209 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-11-17 20:41:50.637 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-11-24 20:42:18.833 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-12-01 20:40:24.422 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-12-08 20:45:27.535 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-12-15 20:46:46.109 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-12-22 20:44:36.189 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-12-29 20:46:01.026 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1727533083.381524 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc.clk.short.png "Recent corrections")

