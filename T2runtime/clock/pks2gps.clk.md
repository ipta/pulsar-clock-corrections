
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
| Original download URL | <https://www.parkes.atnf.csiro.au/observing/clockfiles/pks2gps.clk.20250601> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1858-11-17 MJD 0.0 |
| Clock file end | 2025-05-31 MJD 60826.1 |
| Update interval (days) | 7 |
| Last update attempt | 2025-07-21 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2025-05-19 20:42:16.398 - Updated
2025-05-26 20:41:07.508 - Unchanged
2025-06-02 20:43:50.747 - Unchanged
2025-06-09 20:44:01.470 - Unchanged
2025-06-16 20:43:53.385 - Unchanged
2025-06-23 20:43:54.974 - Updated
2025-06-30 20:43:34.639 - Unchanged
2025-07-07 20:44:33.889 - Unchanged
2025-07-14 20:44:54.749 - Unchanged
2025-07-21 20:45:26.956 - Unchanged
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

