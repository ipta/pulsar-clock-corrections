
## Meerkat (TEMPO2)

MeerKAT clock corrections file (TEMPO2)

This file is pulled from the TEMPO2 repository and may not be fully up-to-date.

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
| Last update attempt | 2022-08-31 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-06-29 20:36:10.647 - Unchanged
2022-07-06 20:33:10.634 - Unchanged
2022-07-13 20:34:16.550 - Unchanged
2022-07-20 20:36:49.303 - Unchanged
2022-07-27 20:33:04.002 - Unchanged
2022-08-03 20:34:48.988 - Unchanged
2022-08-10 20:34:08.989 - Unchanged
2022-08-17 20:34:06.331 - Unchanged
2022-08-24 20:34:39.370 - Unchanged
2022-08-31 20:34:58.692 - Unchanged
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

