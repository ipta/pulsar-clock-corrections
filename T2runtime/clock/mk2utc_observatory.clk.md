
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
| Clock file end | 2024-04-24 MJD 60425.0 |
| Update interval (days) | 7 |
| Last update attempt | 2024-06-28 |
| Last update result | Failed to download |

Log entries from the last few update attempts:
```
2024-04-11 20:29:40.709 - Unchanged
2024-04-18 20:29:46.133 - Updated
2024-05-10 20:29:48.819 - Updated
2024-05-17 20:29:50.578 - Unchanged
2024-05-24 20:29:41.581 - Unchanged
2024-05-31 20:29:41.668 - Unchanged
2024-06-07 20:29:36.289 - Unchanged
2024-06-14 20:29:57.559 - Unchanged
2024-06-21 20:29:58.849 - Unchanged
2024-06-28 20:29:55.029 - Failed to download: <urlopen error _ssl.c:990: The handshake operation timed out>
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1714475549.195445 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

