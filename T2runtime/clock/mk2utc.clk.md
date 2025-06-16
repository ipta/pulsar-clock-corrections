
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
| Last update attempt | 2025-06-16 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2025-01-29 20:35:53.683 - Unchanged
2025-02-05 20:37:16.268 - Unchanged
2025-02-12 20:36:47.399 - Unchanged
2025-05-05 14:31:08.686 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-05-12 20:38:57.406 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-05-19 20:42:23.008 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-05-26 20:41:15.585 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-06-02 20:44:05.618 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-06-09 20:44:07.749 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
2025-06-16 20:44:25.349 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 8252 places
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

