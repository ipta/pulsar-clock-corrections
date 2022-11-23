
## VLA to NIST

Very Large Array to NIST clock corrections (TEMPO2)

This file is pulled from the TEMPO2 repository and may not be fully up-to-date.

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
| Last update attempt | 2022-11-23 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-09-21 20:38:53.654 - Unchanged
2022-09-28 20:41:26.759 - Unchanged
2022-10-05 20:42:16.288 - Unchanged
2022-10-12 20:43:16.357 - Unchanged
2022-10-19 20:43:37.784 - Unchanged
2022-10-26 20:37:22.017 - Unchanged
2022-11-02 20:34:11.783 - Unchanged
2022-11-09 20:34:50.269 - Unchanged
2022-11-16 20:33:01.145 - Unchanged
2022-11-23 20:30:49.223 - Unchanged
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

