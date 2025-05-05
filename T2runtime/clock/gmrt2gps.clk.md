
## GMRT

GMRT (null) clock corrections

The GMRT records data directly against GPS time, and thus no clock
corrections are necessary. This file is a placeholder to make that
obvious.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/gmrt2gps.clk` |
| Authority | observatory |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/gmrt2gps.clk> |
| Original download URL | <None> |
| Format | tempo2 |
| Bogus last correction | True |
| Clock file start | --- |
| Clock file end | --- |
| Update interval (days) | inf |
| Last update attempt | 2025-05-05 |
| Last update result | No way to download |

Log entries from the last few update attempts:
```
2022-06-01 12:20:21.838 - Failed to download: HTTP Error 404: Not Found
2025-05-05 17:53:46.839 - No way to download: 'T2runtime/clock/gmrt2gps.clk'
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/gmrt2gps.clk.log)

Leading comments from clock file:

    # The GMRT references its data directly to GPS time and therefore
    # requires no clock corrections. This file exists to make that
    # explicit.



All clock corrections:

![plot of all clock corrections](gmrt2gps.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](gmrt2gps.clk.short.png "Recent corrections")

