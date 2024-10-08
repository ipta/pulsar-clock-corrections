
## Parkes

Parkes observatory clock corrections

This file is pulled from the Parkes observatory repository and should 
be up-to-date.

The comments read:

    Tie of Parkes clock to GPS time standard. Sources are listed below.
    Where two clock systems existed simultaneously, the dates refer to
    periods when the given clock was supplied as the observatory 1 PPS

    (before this, clock was tied to Tidbinbilla clock: see pks2tid.clk)
    MJD 50844    - 52311.17     Mark IV clock vs Totally Accurate Clock (GPS)
                                  from: update_clkcorr -t pksgps4 gps??.dat
    MJD 52311.17 - now          Mark VI clock vs GPS East
                                  from: update_clkcorr -t pksgps6 pkclk00.*
    -- Russell Edwards 24 September 2004

The file includes a first entry on MJD 0.00521 with a clock
correction of 1.04 us; while normally we automatically ignore MJD 0
for plotting purposes, this value must be in there for a reason so
we retain it.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/pks2gps.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/pks2gps.clk> |
| Original download URL | <https://www.parkes.atnf.csiro.au/observing/clockfiles/pks2gps.clk.20241001> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1858-11-17 MJD 0.0 |
| Clock file end | 2024-08-31 MJD 60553.1 |
| Update interval (days) | 7 |
| Last update attempt | 2024-10-04 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2024-08-02 20:31:14.898 - Unchanged
2024-08-09 20:31:07.759 - Updated
2024-08-16 20:31:04.055 - Unchanged
2024-08-23 20:30:58.744 - Unchanged
2024-08-30 20:32:33.292 - Unchanged
2024-09-06 20:31:30.024 - Unchanged
2024-09-13 20:32:07.824 - Updated
2024-09-20 20:33:31.516 - Unchanged
2024-09-27 20:33:24.237 - Unchanged
2024-10-04 20:33:16.183 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/pks2gps.clk.log)

Leading comments from clock file:

    #
    # Tie of Parkes clock to GPS time standard. Sources are listed below.
    # Where two clock systems existed simultaneously, the dates refer to
    # periods when the given clock was supplied as the observatory 1 PPS
    #
    # (before this, clock was tied to Tidbinbilla clock: see pks2tid.clk)
    # MJD 50844    - 52311.17     Mark IV clock vs Totally Accurate Clock (GPS)
    #                               from: update_clkcorr -t pksgps4 gps??.dat
    # MJD 52311.17 - now          Mark VI clock vs GPS East
    #                               from: update_clkcorr -t pksgps6 pkclk00.*
    # -- Russell Edwards 24 September 2004
    #-------------------------------------------------------------------------



All clock corrections:

![plot of all clock corrections](pks2gps.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](pks2gps.clk.short.png "Recent corrections")

