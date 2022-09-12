
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
| Clock file end | 2022-08-17 MJD 59809.0 |
| Update interval (days) | 7 |
| Last update attempt | 2022-09-12 |
| Last update result | Failed to download |

Log entries from the last few update attempts:
```
2022-07-11 20:34:36.789 - Updated
2022-07-18 20:34:30.484 - Unchanged
2022-07-25 20:33:31.267 - Updated
2022-08-01 20:37:43.896 - Unchanged
2022-08-08 20:35:15.765 - Updated
2022-08-15 20:34:21.731 - Failed to download: The read operation timed out
2022-08-22 20:33:37.370 - Unchanged
2022-08-29 20:35:28.170 - Updated
2022-09-05 20:35:40.782 - Failed to download: The read operation timed out
2022-09-12 20:38:32.955 - Failed to download: The read operation timed out
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1661410454.885244 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

