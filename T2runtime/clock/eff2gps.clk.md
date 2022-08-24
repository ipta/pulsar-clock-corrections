
## Effelsberg

Effelsberg telescope clock corrections

This file is pulled from the TEMPO2 repository and may not be fully up-to-date.

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
| Last update attempt | 2022-08-24 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-06-22 20:32:54.256 - Unchanged
2022-06-29 20:36:09.512 - Unchanged
2022-07-06 20:33:10.012 - Unchanged
2022-07-13 20:34:16.001 - Unchanged
2022-07-20 20:36:48.718 - Unchanged
2022-07-27 20:33:02.659 - Unchanged
2022-08-03 20:34:47.791 - Unchanged
2022-08-10 20:34:07.552 - Unchanged
2022-08-17 20:34:05.696 - Unchanged
2022-08-24 20:34:38.076 - Unchanged
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

