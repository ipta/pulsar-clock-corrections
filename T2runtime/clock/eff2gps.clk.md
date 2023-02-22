
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
| Last update attempt | 2023-02-22 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-12-21 20:28:15.588 - Unchanged
2022-12-28 20:27:39.358 - Unchanged
2023-01-04 20:29:17.831 - Unchanged
2023-01-11 20:29:44.204 - Unchanged
2023-01-18 20:29:08.487 - Unchanged
2023-01-25 20:28:09.642 - Unchanged
2023-02-01 20:29:16.779 - Unchanged
2023-02-08 20:29:41.468 - Unchanged
2023-02-15 20:29:55.952 - Unchanged
2023-02-22 20:30:00.958 - Unchanged
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

