
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
| Last update attempt | 2024-04-01 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-01-29 20:29:41.258 - Unchanged
2024-02-05 20:29:37.004 - Unchanged
2024-02-12 20:29:41.883 - Unchanged
2024-02-19 20:29:36.931 - Unchanged
2024-02-26 20:29:29.276 - Unchanged
2024-03-04 20:29:26.330 - Unchanged
2024-03-11 20:29:31.850 - Unchanged
2024-03-18 20:29:24.846 - Unchanged
2024-03-25 20:29:36.573 - Unchanged
2024-04-01 20:29:31.083 - Unchanged
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

