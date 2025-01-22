
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
| Clock file end | 2024-12-05 MJD 60650.0 |
| Update interval (days) | 7 |
| Last update attempt | 2025-01-22 |
| Last update result | Failed to download |

Log entries from the last few update attempts:
```
2024-10-11 20:39:13.519 - Failed to download: HTTP Error 403: Forbidden
2024-11-27 20:39:59.127 - Failed to download: HTTP Error 403: Forbidden
2024-12-04 20:40:30.649 - Failed to download: HTTP Error 403: Forbidden
2024-12-11 20:40:46.813 - Failed to download: HTTP Error 403: Forbidden
2024-12-18 20:39:27.691 - Failed to download: HTTP Error 403: Forbidden
2024-12-25 20:35:18.261 - Failed to download: HTTP Error 403: Forbidden
2025-01-01 20:35:40.302 - Failed to download: HTTP Error 403: Forbidden
2025-01-08 20:37:07.662 - Failed to download: The read operation timed out
2025-01-15 20:35:17.790 - Updated
2025-01-22 20:35:17.843 - Failed to download: <urlopen error _ssl.c:989: The handshake operation timed out>
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1733988385.186672 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

