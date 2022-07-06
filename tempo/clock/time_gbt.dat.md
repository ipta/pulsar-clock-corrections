
## GBT

Green Bank Telescope clock correction file

This file records the difference between UTC(GBT) and UTC(GPS).

The observatory distributes this file on the Web, updated about daily.

If questions arise, contact Ryan S. Lynch <rlynch@nrao.edu>.

|     |     |
|:--- |:--- |
| File | `tempo/clock/time_gbt.dat` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/tempo/clock/time_gbt.dat> |
| Original download URL | <https://www.gb.nrao.edu/~fghigo/timer/time_gbt.dat> |
| Format | tempo |
| Bogus last correction | False |
| Clock file start | 2000-12-31 MJD 51909.5 |
| Clock file end | 2022-07-05 MJD 59765.5 |
| Update interval (days) | 1 |
| Last update attempt | 2022-07-06 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2022-06-28 20:35:07.521 - Updated
2022-06-29 20:36:06.141 - Updated
2022-06-30 20:34:24.619 - Updated
2022-07-01 20:35:04.541 - Updated
2022-07-02 20:32:17.135 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
2022-07-03 20:31:45.869 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
2022-07-04 14:49:32.673 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
2022-07-04 14:49:32.674 - Updated overriding validation failure
2022-07-05 20:34:42.061 - Updated
2022-07-06 20:33:07.912 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)


All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

