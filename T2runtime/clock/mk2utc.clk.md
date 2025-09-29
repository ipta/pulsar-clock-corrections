
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
| Last update attempt | 2025-09-29 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2025-07-28 20:46:36.482 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-08-04 20:47:32.845 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-08-11 20:42:56.476 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-08-18 20:41:43.006 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-08-25 20:42:36.637 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-09-01 20:38:36.267 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-09-08 20:40:40.602 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-09-15 20:38:24.488 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-09-22 20:40:21.203 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-09-29 20:37:24.227 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
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

