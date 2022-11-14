
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
| Clock file end | 2022-10-27 MJD 59880.0 |
| Update interval (days) | 7 |
| Last update attempt | 2022-11-14 |
| Last update result | Updated |

Log entries from the last few update attempts:
```
2022-09-12 20:38:32.955 - Failed to download: The read operation timed out
2022-09-19 20:40:34.403 - Updated
2022-09-26 20:39:35.311 - Failed to download: The read operation timed out
2022-10-03 20:42:23.768 - Failed to download: The read operation timed out
2022-10-10 20:41:57.569 - Updated
2022-10-17 20:42:44.233 - Updated
2022-10-24 20:43:28.588 - Unchanged
2022-10-31 20:38:02.379 - Failed to download: <urlopen error _ssl.c:1114: The handshake operation timed out>
2022-11-07 20:36:05.762 - Failed to download: <urlopen error _ssl.c:980: The handshake operation timed out>
2022-11-14 20:34:27.545 - Updated
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1667372572.887767 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

