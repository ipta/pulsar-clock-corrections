
## LEAP

LEAP clock correction file

This file corrects from the LEAP clock to the Effelsberg Asterix
clock; then the effix2gps file can be used to convert to GPS.

This file is pulled from the TEMPO2 repository and may not be fully
up-to-date. The European Pulsar Timing Array maintains an internal
repository of clock corrections, which they have transferred to the TEMPO2
repository, so  EPTA telescope data in the TEMPO2 repository (and
thus here) can be expected to be somewhat up to date.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/leap2effix.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/leap2effix.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/leap2effix.clk> |
| Format | tempo2 |
| Bogus last correction | True |
| Clock file start | 2012-10-29 MJD 56230.0 |
| Clock file end | 2014-03-04 MJD 56720.0 |
| Update interval (days) | 7 |
| Last update attempt | 2024-06-07 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-03-21 20:29:49.526 - Unchanged
2024-03-28 20:29:39.741 - Unchanged
2024-04-04 20:29:36.456 - Unchanged
2024-04-11 20:29:35.144 - Unchanged
2024-04-18 20:29:39.225 - Unchanged
2024-05-10 20:29:44.505 - Unchanged
2024-05-17 20:29:46.841 - Unchanged
2024-05-24 20:29:37.569 - Unchanged
2024-05-31 20:29:35.341 - Unchanged
2024-06-07 20:29:33.210 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/leap2effix.clk.log)

Leading comments from clock file:

    # Some 'effix' time jumps do not appear in LEAP data
    # So we must account for this...
    #    MJD: 56230 to 56490; offset=-0.0972843 s * pre-removed in LEAP
    #    MJD: 56490 to 56720; offset=-0.409268 s * pre-removed in LEAP
    #



All clock corrections:

![plot of all clock corrections](leap2effix.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](leap2effix.clk.short.png "Recent corrections")

