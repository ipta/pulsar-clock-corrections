
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
| Last update attempt | 2024-10-04 |
| Last update result | Failed to download |

Log entries from the last few update attempts:
```
2024-08-02 20:31:19.452 - Failed to download: HTTP Error 403: Forbidden
2024-08-09 20:31:14.076 - Failed to download: HTTP Error 403: Forbidden
2024-08-16 20:31:06.018 - Failed to download: HTTP Error 403: Forbidden
2024-08-23 20:31:02.824 - Failed to download: HTTP Error 502: Proxy Error
2024-08-30 20:32:35.880 - Failed to download: HTTP Error 403: Forbidden
2024-09-06 20:31:43.821 - Failed to download: The read operation timed out
2024-09-13 20:32:10.289 - Failed to download: HTTP Error 403: Forbidden
2024-09-20 20:33:35.218 - Validation failed: Unable to read new version of T2runtime/clock/mk2utc_observatory.clk: Header line must start with # and contain two time scales: 'The SARAO archive is currently down. We apologise for the inconvenience. We will remove this alert once the archive is available again.\n'
2024-09-27 20:33:26.829 - Failed to download: HTTP Error 403: Forbidden
2024-10-04 20:33:22.425 - Failed to download: HTTP Error 403: Forbidden
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

