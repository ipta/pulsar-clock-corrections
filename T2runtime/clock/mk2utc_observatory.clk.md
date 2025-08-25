
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
| Clock file end | 2025-08-01 MJD 60889.0 |
| Update interval (days) | 7 |
| Last update attempt | 2025-08-25 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2025-06-23 20:44:08.669 - Updated
2025-06-30 20:43:39.919 - Unchanged
2025-07-07 20:44:46.829 - Failed to download: <urlopen error _ssl.c:999: The handshake operation timed out>
2025-07-14 20:45:02.678 - Unchanged
2025-07-21 20:45:50.761 - Unchanged
2025-07-28 20:46:35.112 - Updated
2025-08-04 20:47:31.397 - Failed to download: <urlopen error _ssl.c:999: The handshake operation timed out>
2025-08-11 20:42:54.993 - Updated
2025-08-18 20:41:41.526 - Unchanged
2025-08-25 20:42:34.702 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1754484025.142011 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

