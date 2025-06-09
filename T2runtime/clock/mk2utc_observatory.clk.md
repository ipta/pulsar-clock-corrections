
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
| Clock file end | 2025-05-20 MJD 60816.0 |
| Update interval (days) | 7 |
| Last update attempt | 2025-06-09 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2025-01-22 20:35:17.843 - Failed to download: <urlopen error _ssl.c:989: The handshake operation timed out>
2025-01-29 20:35:52.603 - Updated
2025-02-05 20:37:15.621 - Updated
2025-02-12 20:36:46.761 - Unchanged
2025-05-05 14:31:07.654 - Updated
2025-05-12 20:38:56.123 - Updated
2025-05-19 20:42:21.702 - Unchanged
2025-05-26 20:41:14.027 - Updated
2025-06-02 20:44:03.921 - Failed to download: <urlopen error _ssl.c:999: The handshake operation timed out>
2025-06-09 20:44:06.297 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1748250355.847543 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

