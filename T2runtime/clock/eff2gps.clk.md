
## Effelsberg

Effelsberg telescope clock corrections

This file is pulled from the TEMPO2 repository and may not be fully
up-to-date.

Originally made from time_bonn.dat with an awk script, according to
the comments.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/eff2gps.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/eff2gps.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/eff2gps.clk> |
| Format | tempo2 |
| Bogus last correction | True |
| Clock file start | 1993-11-29 MJD 49320.0 |
| Clock file end | 2015-06-22 MJD 57195.5 |
| Update interval (days) | 7 |
| Last update attempt | 2025-09-15 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2025-07-14 20:44:55.496 - Unchanged
2025-07-21 20:45:37.290 - Unchanged
2025-07-28 20:46:20.913 - Unchanged
2025-08-04 20:47:20.140 - Unchanged
2025-08-11 20:42:49.821 - Unchanged
2025-08-18 20:41:37.069 - Unchanged
2025-08-25 20:42:29.423 - Unchanged
2025-09-01 20:38:28.325 - Unchanged
2025-09-08 20:40:35.155 - Unchanged
2025-09-15 20:38:19.855 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/eff2gps.clk.log)

Leading comments from clock file:

    # From old tempo time_bonn.dat:
    # awk '{printf("%11.5f %10.5e\n",$1,$3/1.e6)}' time_bonn.dat
    #  > $TEMPO2/clock/eff2gps.clk
    #



All clock corrections:

![plot of all clock corrections](eff2gps.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](eff2gps.clk.short.png "Recent corrections")

