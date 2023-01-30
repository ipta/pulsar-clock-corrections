
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
| Clock file end | 2023-01-04 MJD 59949.0 |
| Update interval (days) | 7 |
| Last update attempt | 2023-01-30 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-11-28 20:30:26.511 - Failed to download: The read operation timed out
2022-12-05 20:29:52.264 - Unchanged
2022-12-12 20:29:29.623 - Failed to download: The read operation timed out
2022-12-19 20:29:23.770 - Updated
2022-12-26 20:27:38.627 - Unchanged
2023-01-02 20:27:42.066 - Unchanged
2023-01-09 20:30:52.241 - Unchanged
2023-01-16 20:28:30.474 - Updated
2023-01-23 20:29:04.205 - Unchanged
2023-01-30 20:29:13.623 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/mk2utc_observatory.clk.log)

Leading comments from clock file:

    # Tie of Karoo Telescope Time to UTC
    # This file is from the KTT-GNSS sensor, and does not include circular-T
    # MJD = (SensorTime(us)/86400e6)+40587    15-minute snapshots
    # Created at unix time 1673420671.172928 from KTT mySQL database.
    #
    # MJD (days)   KTT-UTC (seconds)
    #------------------------------------------------------



All clock corrections:

![plot of all clock corrections](mk2utc_observatory.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](mk2utc_observatory.clk.short.png "Recent corrections")

