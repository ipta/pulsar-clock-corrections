
## Meerkat (observatory)

MeerKAT clock corrections file

This file is distributed by the observatory. It records the local
clock difference from (I think) GPS. It may cause some problems
for TEMPO2 as it has a header line "# UTC(MK) UTC" when TEMPO2
would expect "# UTC(meerkat) UTC" or "# UTC(meerkat) UTC(GPS)".

If questions arise, contact Ryan Shannon <rshannon@swin.edu.au>

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/mk2utc_observatory.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/mk2utc_observatory.clk> |
| Original download URL | <https://archive-gw-1.kat.ac.za/public/tfr/mk2utc.clk> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 2019-01-01 MJD 58484.0 |
| Clock file end | 2024-04-04 MJD 60405.0 |
| Update interval (days) | 7 |
| Last update attempt | 2024-04-18 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2024-02-15 20:30:01.644 - Unchanged
2024-02-22 20:30:01.784 - Unchanged
2024-02-29 20:29:42.096 - Unchanged
2024-03-07 20:30:06.819 - Unchanged
2024-03-14 20:29:41.493 - Unchanged
2024-03-21 20:29:53.172 - Unchanged
2024-03-28 20:29:51.405 - Unchanged
2024-04-04 20:29:44.899 - Unchanged
2024-04-11 20:29:40.709 - Unchanged
2024-04-18 20:29:46.133 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1712738994.715545 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

