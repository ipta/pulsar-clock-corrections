
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
<anne.archibald@nanograv.org>. For more detailed questions
about the BIPM's published corrections, contact <tai@bipm.org>.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/gps2utc_cc.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/gps2utc_cc.clk> |
| Original download URL | <None> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1993-01-01 MJD 48988.0 |
| Clock file end | 2024-11-30 MJD 60644.0 |
| Update interval (days) | 1 |
| Last update attempt | 2024-12-22 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-12-13 20:39:56.850 - Unchanged
2024-12-14 20:37:32.263 - Unchanged
2024-12-15 20:37:17.908 - Unchanged
2024-12-16 20:40:27.975 - Unchanged
2024-12-17 20:37:39.574 - Unchanged
2024-12-18 20:39:07.243 - Unchanged
2024-12-19 20:36:39.982 - Unchanged
2024-12-20 20:36:04.654 - Unchanged
2024-12-21 20:34:06.334 - Unchanged
2024-12-22 20:34:18.743 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/gps2utc_cc.clk.log)

Leading comments from clock file:

    # Corrections from UTC inferred from the GPS Combined Clock to UTC.
    # Leap seconds do not appear here, and the Combined Clock is steered
    # to try to make it approximate UTC, but there is some residual drift.
    #
    # Note that the GPS "almanac" signal also includes predictions of its
    # deviations from UTC, so the Combined Clock is not necessarily the best
    # available approximation of UTC; a suitable receiver can do better.
    #
    # The BIPM publishes these values as "C0", from about 1995 to the present.
    # The BIPM also publishes corrections for the predicted UTC, but only from
    # 2011. Those are available in a separate file.
    #
    # The first values in this file are from the BIPM yearly summary tables
    # available for years YY=93 to 03 from
    # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPS/utcgpsYY.ar
    # and for years YY=03 to 11 from
    # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPSGLO/utcgpsgloYY.ar
    # Later entries in the file (there is a comment to mark the place)
    # are obtained from
    # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gps
    # which is updated monthly.
    #



All clock corrections:

![plot of all clock corrections](gps2utc_cc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gps2utc_cc.clk.short.png "Recent corrections")

