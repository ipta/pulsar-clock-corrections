
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
| Clock file end | 2022-07-31 MJD 59791.5 |
| Update interval (days) | 1 |
| Last update attempt | 2022-08-04 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2022-07-26 20:32:24.915 - Updated
2022-07-27 20:32:57.847 - Updated
2022-07-28 20:35:28.429 - Updated
2022-07-29 20:35:58.517 - Updated
2022-07-30 20:32:10.621 - Updated
2022-07-31 20:33:29.410 - Updated
2022-08-01 20:37:40.878 - Updated
2022-08-02 20:33:42.762 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
2022-08-03 20:34:43.782 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
2022-08-04 20:34:37.508 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 1 places
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)


All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

