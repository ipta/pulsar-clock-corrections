
## GPS to UTC (Corrected)

GPS to UTC clock corrections (Corrected)

This file is constructed from BIPM published data and should be up-to-date.

The BIPM publishes two different corrections from GPS to UTC:
the first, C0, corrects from the GPS Combined Clock to UTC. The second,
C0', corrects from a timescale that takes advantage of the broadcast
GPS almanac data to track UTC more closely.

This file uses C0' data, that is, it is for GPS time standards that
take advantage of the almanac data to improve their time correction.
Unfortunately the BIPM only publishes these corrections going back
to 2011.

If you have questions about this, contact Anne Archibald
<anne.archibald@nanograv.org>. For more detailed questions
about the BIPM's published corrections, contact <tai@bipm.org>.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/gps2utc_c0p.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/gps2utc_c0p.clk> |
| Original download URL | <None> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 2010-12-29 MJD 55559.0 |
| Clock file end | 2025-08-27 MJD 60914.0 |
| Update interval (days) | 1 |
| Last update attempt | 2025-09-27 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2025-09-18 20:39:48.644 - Unchanged
2025-09-19 20:38:39.719 - Unchanged
2025-09-20 20:35:28.203 - Unchanged
2025-09-21 20:36:55.842 - Unchanged
2025-09-22 20:39:58.154 - Unchanged
2025-09-23 20:40:03.712 - Unchanged
2025-09-24 20:38:47.064 - Unchanged
2025-09-25 20:39:39.185 - Unchanged
2025-09-26 20:38:51.374 - Unchanged
2025-09-27 20:32:45.085 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/gps2utc_c0p.clk.log)

Leading comments from clock file:

    # Corrections from the GPS predictions of UTC to UTC.
    # Leap seconds do not appear here.
    #
    # Note that the GPS "almanac" signal also includes predictions of the
    # Combined Clock's deviations from UTC, so a suitable receiver can produce a
    # good approximation of UTC. This file records the errors in that approximation.
    #
    # The BIPM publishes these values as "C0'", from about 2011 to the present.
    # The BIPM also publishes corrections for the Combined Clock, going back to
    # 1993. Those are available in a separate file.
    #
    # The data in this file is obtained from
    # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gps
    # which is updated monthly.
    #



All clock corrections:

![plot of all clock corrections](gps2utc_c0p.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gps2utc_c0p.clk.short.png "Recent corrections")

