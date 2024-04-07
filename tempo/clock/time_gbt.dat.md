
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
| Clock file end | 2024-04-06 MJD 60406.5 |
| Update interval (days) | 1 |
| Last update attempt | 2024-04-07 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2024-03-29 20:29:23.228 - Updated
2024-03-30 20:29:49.276 - Updated
2024-03-31 20:29:38.244 - Updated
2024-04-01 20:29:30.458 - Updated
2024-04-02 20:30:02.334 - Updated
2024-04-03 20:29:21.936 - Updated
2024-04-04 20:29:26.874 - Updated
2024-04-05 20:29:19.221 - Updated
2024-04-06 20:29:47.527 - Updated
2024-04-07 20:29:29.776 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)


All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

