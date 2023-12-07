
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
| Clock file end | 2023-10-18 MJD 60235.9 |
| Update interval (days) | 7 |
| Last update attempt | 2023-12-04 |
| Last update result | Updated overriding validation failure |

Log entries from the last few update attempts:
```
2023-03-01 20:30:53.755 - Unchanged
2023-03-08 20:30:17.025 - Unchanged
2023-03-15 20:29:36.706 - Unchanged
2023-03-22 20:26:18.528 - Unchanged
2023-03-29 20:28:32.380 - Unchanged
2023-04-05 20:28:50.634 - Unchanged
2023-04-12 20:26:24.229 - Unchanged
2023-12-04 18:55:35.017 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 597 places
2023-12-04 21:02:53.225 - Validation failed: New version of T2runtime/clock/mk2utc.clk MJDs differ from old version where they overlap in 597 places
2023-12-04 21:02:53.228 - Updated overriding validation failure
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1698127044.80721 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc.clk.short.png "Recent corrections")

