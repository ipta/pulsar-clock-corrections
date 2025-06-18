
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
| Clock file end | 2025-06-14 MJD 60840.5 |
| Update interval (days) | 1 |
| Last update attempt | 2025-06-18 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2025-06-09 20:43:53.054 - Updated
2025-06-10 20:43:48.320 - Updated
2025-06-11 20:43:11.467 - Updated
2025-06-12 20:43:38.318 - Updated
2025-06-13 20:43:07.594 - Updated
2025-06-14 20:40:10.165 - Updated
2025-06-15 20:41:25.219 - Unchanged
2025-06-16 20:43:44.193 - Unchanged
2025-06-17 20:43:17.522 - Validation failed: New version of tempo/clock/time_gbt.dat clock corrections differ from old version where they overlap in 6 places
2025-06-18 20:44:24.694 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)

Leading comments from clock file:

     -2271.50       0.0        -0.486 1    32767-dec



All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

