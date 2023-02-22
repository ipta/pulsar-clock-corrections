
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
| Clock file end | 2021-02-22 MJD 59268.0 |
| Update interval (days) | 7 |
| Last update attempt | 2023-02-22 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-12-21 20:28:16.762 - Unchanged
2022-12-28 20:27:39.834 - Unchanged
2023-01-04 20:29:18.344 - Unchanged
2023-01-11 20:29:44.626 - Unchanged
2023-01-18 20:29:09.691 - Unchanged
2023-01-25 20:28:10.140 - Unchanged
2023-02-01 20:29:17.191 - Unchanged
2023-02-08 20:29:42.893 - Unchanged
2023-02-15 20:29:56.419 - Unchanged
2023-02-22 20:30:01.392 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1614080015.929991 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc.clk.short.png "Recent corrections")

