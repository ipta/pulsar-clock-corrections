
## VLA to NIST

Very Large Array to NIST clock corrections (TEMPO2)

This file is pulled from the TEMPO2 repository and may not be fully
up-to-date.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/vla2nist.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/vla2nist.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/vla2nist.clk> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1990-10-27 MJD 48191.2 |
| Clock file end | 1993-11-13 MJD 49304.0 |
| Update interval (days) | 7 |
| Last update attempt | 2024-05-10 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-02-22 20:29:51.704 - Unchanged
2024-02-29 20:29:31.099 - Unchanged
2024-03-07 20:29:56.660 - Unchanged
2024-03-14 20:29:28.107 - Unchanged
2024-03-21 20:29:41.246 - Unchanged
2024-03-28 20:29:33.041 - Unchanged
2024-04-04 20:29:29.966 - Unchanged
2024-04-11 20:29:28.524 - Unchanged
2024-04-18 20:29:32.888 - Unchanged
2024-05-10 20:29:36.977 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/vla2nist.clk.log)

Leading comments from clock file:

    # From old tempo time_vla.dat:
    # awk '$1<50000 {printf("%11.5f %10.5e\n",$1,($3-$2)/1.e6)}' time_vla.dat
    #  > $TEMPO2/clock/vla2nist.clk
    #



All clock corrections:

![plot of all clock corrections](vla2nist.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](vla2nist.clk.short.png "Recent corrections")

