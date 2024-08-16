
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
| Last update attempt | 2024-08-16 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-06-14 20:29:58.528 - Unchanged
2024-06-21 20:29:59.124 - Unchanged
2024-06-28 20:29:55.476 - Unchanged
2024-07-05 20:30:08.604 - Unchanged
2024-07-12 20:29:44.937 - Unchanged
2024-07-19 20:31:14.616 - Unchanged
2024-07-26 20:31:14.851 - Unchanged
2024-08-02 20:31:20.214 - Unchanged
2024-08-09 20:31:14.567 - Unchanged
2024-08-16 20:31:06.489 - Unchanged
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

