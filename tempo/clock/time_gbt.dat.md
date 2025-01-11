
## GBT

Green Bank Telescope clock correction file

This file records the difference between UTC(GBT) and UTC(GPS).

The observatory distributes this file on the Web, updated about daily.

A discrepancy arose between the observatory-distributed file and the
file in this repository (which had been identical to the 
observatory-distributed one up to that point). Around 
2023-03-20 (MJD 60023), the first ~11 entries in the 
observatory-distributed file were changed to zero.
Ryan Lynch expressed surprise that this had occurred, but no
resolution had arisen as of 2024-02-14. Since this resulted in
the new file failing validation and the file in this repository
not updating, at that point I (Anne Archibald) decided to
switch those entries to match the observatory values. The old values
are available from the version of the file in git tag 
"gbt-mystery-values".

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
| Clock file end | 2024-05-18 MJD 60448.5 |
| Update interval (days) | 1 |
| Last update attempt | 2025-01-11 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2025-01-02 20:36:21.150 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-03 20:35:31.406 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-04 20:34:28.268 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-05 20:34:24.272 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-06 20:35:01.444 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-07 20:36:07.109 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-08 20:36:44.963 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-09 20:36:52.909 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-10 20:36:44.569 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-01-11 20:34:26.970 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)


All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

