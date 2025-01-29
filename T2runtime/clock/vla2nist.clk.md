
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
| Last update attempt | 2025-01-29 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-11-27 20:39:49.470 - Unchanged
2024-12-04 20:40:22.509 - Unchanged
2024-12-11 20:40:36.351 - Unchanged
2024-12-18 20:39:19.315 - Unchanged
2024-12-25 20:35:02.276 - Unchanged
2025-01-01 20:35:26.576 - Unchanged
2025-01-08 20:36:49.238 - Unchanged
2025-01-15 20:34:58.806 - Unchanged
2025-01-22 20:35:00.312 - Unchanged
2025-01-29 20:35:41.255 - Unchanged
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

