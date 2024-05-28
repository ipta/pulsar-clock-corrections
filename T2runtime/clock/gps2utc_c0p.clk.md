
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
| Clock file end | 2024-04-29 MJD 60429.0 |
| Update interval (days) | 1 |
| Last update attempt | 2024-05-28 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-05-19 20:29:30.555 - Unchanged
2024-05-20 20:29:25.651 - Unchanged
2024-05-21 20:29:31.762 - Unchanged
2024-05-22 20:29:34.408 - Unchanged
2024-05-23 20:29:32.587 - Unchanged
2024-05-24 20:29:27.908 - Unchanged
2024-05-25 20:29:17.160 - Unchanged
2024-05-26 20:29:30.702 - Unchanged
2024-05-27 20:29:39.388 - Unchanged
2024-05-28 20:29:17.178 - Unchanged
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
    # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss
    # which is updated monthly.
    #



All clock corrections:

![plot of all clock corrections](gps2utc_c0p.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gps2utc_c0p.clk.short.png "Recent corrections")

