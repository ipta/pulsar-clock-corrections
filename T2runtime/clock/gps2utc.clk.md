
## GPS to UTC

GPS to UTC clock corrections

This file is constructed from BIPM published data and should be up-to-date.

The BIPM publishes two different corrections from GPS to UTC:
the first, C0, corrects from the GPS Combined Clock to UTC. The second,
C0', corrects from a timescale that takes advantage of the broadcast
GPS almanac data to track UTC more closely.

This file uses C0' data when available, but that is only since 2011.
Prior to that this uses C0.

You may want to consider whether your GPS time standard is returning
the Combined Clock or whether it is using the almanac data. There are
more specific correction files suitable for one case or the other.

If you have questions about this, contact Anne Archibald
<anne.archibald@newcastle.ac.uk>. For more detailed questions
about the BIPM's published corrections, contact <tai@bipm.org>.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/gps2utc.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/gps2utc.clk> |
| Original download URL | <None> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1993-01-01 MJD 48988.0 |
| Clock file end | 2022-06-29 MJD 59759.0 |
| Update interval (days) | 1 |
| Last update attempt | 2022-08-23 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2022-08-14 20:32:47.578 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-15 20:34:09.272 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-16 20:33:21.815 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-17 20:34:02.917 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-18 20:36:44.551 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-19 20:35:01.671 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-20 20:33:20.357 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-21 20:33:33.441 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-22 20:33:33.953 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
2022-08-23 20:34:34.032 - Validation failed: New version of T2runtime/clock/gps2utc.clk clock corrections differ from old version where they overlap in 1 places
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/gps2utc.clk.log)

Leading comments from clock file:

    # Corrections from GPS to UTC.
    # Leap seconds do not appear here.
    #
    # Note that the GPS "almanac" signal also includes predictions of the
    # Combined Clock's deviations from UTC, so a suitable receiver can produce a
    # good approximation of UTC.
    #
    # The BIPM publishes these values as "C0'", from about 2011 to the present.
    # The BIPM also publishes corrections for the Combined Clock, going back to
    # 1993. This file contains both: when available, we use C0', before that we
    # use C0. This may or may not resemble what your GPS receiver system uses.
    #
    # The first values in this file are from the BIPM yearly summary tables
    # available for years YY=93 to 03 from
    # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPS/utcgpsYY.ar
    # and for years YY=03 to 11 from
    # ftp://ftp2.bipm.org/pub/tai/scale/UTCGPSGLO/utcgpsgloYY.ar
    # Later entries in the file (there is a comment to mark the place)
    # are obtained from
    # https://webtai.bipm.org/ftp/pub/tai/other-products/utcgnss/utc-gnss
    # which is updated monthly.
    #
    # These entries are based on C0 values.



All clock corrections:

![plot of all clock corrections](gps2utc.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gps2utc.clk.short.png "Recent corrections")

