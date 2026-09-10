
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
| Clock file end | 2026-09-09 MJD 61292.5 |
| Update interval (days) | 1 |
| Last update attempt | 2026-09-10 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2026-09-01 00:00:08.502 - Updated
2026-09-02 22:47:10.844 - Updated
2026-09-03 22:43:29.477 - Updated
2026-09-04 22:29:11.889 - Updated
2026-09-05 22:10:18.883 - Updated
2026-09-06 22:14:43.684 - Updated
2026-09-07 22:57:36.785 - Updated
2026-09-08 22:49:51.826 - Updated
2026-09-09 22:42:05.149 - Updated
2026-09-10 22:44:59.850 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_gbt.dat.log)

Leading comments from clock file:

     -2740.50       0.0        -0.503 1    32764-dec
     -2612.50       0.0        -0.503 1    00-dec-00



All clock corrections:

![plot of all clock corrections](time_gbt.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_gbt.dat.short.png "Recent corrections")

