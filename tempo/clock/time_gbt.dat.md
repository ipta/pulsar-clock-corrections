
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

In May 2024, the values were changed back in the source file.
This resulted in the file failing validation and refusing to update,
again. As of February 2025, this should be fully resolved and the
original values restored, on both ends.

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
| Clock file end | 2025-02-11 MJD 60717.5 |
| Update interval (days) | 1 |
| Last update attempt | 2025-02-12 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2025-02-03 20:35:12.117 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-02-04 20:35:58.203 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-02-05 20:37:00.165 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-02-06 20:35:34.626 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 11 places
2025-02-07 20:35:48.148 - Updated
2025-02-08 20:33:46.179 - Updated
2025-02-09 20:33:00.330 - Updated
2025-02-10 20:36:31.721 - Updated
2025-02-11 20:36:33.614 - Updated
2025-02-12 20:36:25.432 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)


All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

