
## GPS to UTC (Combined Clock)

GPS to UTC clock corrections (Combined Clock)

This file is constructed from BIPM published data and should be up-to-date.

The BIPM publishes two different corrections from GPS to UTC:
the first, C0, corrects from the GPS Combined Clock to UTC. The second,
C0', corrects from a timescale that takes advantage of the broadcast
GPS almanac data to track UTC more closely.

This file uses C0 data, that is, it is for GPS time standards that
do not take advantage of the almanac data to improve their time
correction.

If you have questions about this, contact Anne Archibald
<anne.archibald@newcastle.ac.uk>. For more detailed questions
about the BIPM's published corrections, contact <tai@bipm.org>.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/gps2utc_cc.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/gps2utc_cc.clk> |
| Original download URL | <None> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1993-01-01 MJD 48988.0 |
| Clock file end | 2022-04-30 MJD 59699.0 |
| Update interval (days) | 1 |
| Last update attempt | 2022-06-08 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2022-06-08 10:46:41.912 - No way to download: 'T2runtime/clock/gps2utc_cc.clk'
2022-06-08 10:46:41.942 - Updated
```
[Full log](https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/log/T2runtime/clock/gps2utc_cc.clk.log)


All clock corrections:

![plot of all clock corrections](gps2utc_cc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gps2utc_cc.clk.short.png "Recent corrections")

