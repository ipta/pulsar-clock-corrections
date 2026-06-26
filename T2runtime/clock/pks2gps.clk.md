
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
| Original download URL | <https://www.parkes.atnf.csiro.au/observing/clockfiles/pks2gps.clk.20260401> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1858-11-17 MJD 0.0 |
| Clock file end | 2026-03-31 MJD 61130.1 |
| Update interval (days) | 7 |
| Last update attempt | 2026-06-26 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2026-04-24 21:13:43.142 - Unchanged
2026-05-01 21:14:49.966 - Unchanged
2026-05-08 21:34:58.080 - Unchanged
2026-05-15 21:35:37.521 - Updated
2026-05-22 21:43:17.584 - Unchanged
2026-05-29 22:14:08.594 - Unchanged
2026-06-05 21:54:09.494 - Unchanged
2026-06-12 22:06:16.699 - Unchanged
2026-06-19 21:42:56.655 - Unchanged
2026-06-26 21:48:32.593 - Unchanged
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

