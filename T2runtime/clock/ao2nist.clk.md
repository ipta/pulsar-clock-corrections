
## Arecibo to NIST (TEMPO2)

Arecibo clock corrections to UTC(NIST) (TEMPO2 version)

The early clock corrections for Arecibo predate GPS and are
actually referenced directly to NIST. This clock correction file
separates these out so their corrections can be handled using a
different clock chain.

This file is pulled from the TEMPO2 repository and may not be fully
up-to-date.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/ao2nist.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/ao2nist.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/ao2nist.clk> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1982-11-29 MJD 45302.8 |
| Clock file end | 1994-11-29 MJD 49685.4 |
| Update interval (days) | inf |
| Last update attempt | 2022-05-26 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-05-26 20:40:04.320 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/ao2nist.clk.log)

Leading comments from clock file:

    # From old tempo time_ao.dat:
    # awk '$1<50000 {printf("%11.5f %10.5e\n",$1,($3-$2)/1.e6)}' time_ao.dat
    #  > $TEMPO2/clock/ao2nist.clk
    #



All clock corrections:

![plot of all clock corrections](ao2nist.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](ao2nist.clk.short.png "Recent corrections")


### Further information

- [Description of this repository](index.html)
- [Instructions for using this repository with various software](instructions.html)
- [Status page](status.html)



This repository is currently maintained by Anne Archibald <anne.archibald@nanograv.org>.
