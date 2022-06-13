
## TAI to TT(BIPM2003)

TAI to BIPM-updated TT, 2003 version

This file is constructed from BIPM published data and should
never change; updated versions will appear approximately
yearly, and do revise old data. Aa result they are given different
clock file names, and are treated as different time scales.

The time scale TT is supposed to be a basis for TDB, and is meant
to be a stable clock for describing the motions of the solar system.
Of necessity it is derived from the practical time scale TAI,
which is produced by an ensemble of atomic clocks. A simple
realization of TT, such as that implemented by Astropy,
simply yields TT = TAI + 32.184 s.

Atomic clocks do wander, and the BIPM can sometimes estimate
that wander in retrospect.  Rather than revise TAI, the BIPM
offers versions of TT that are more stable because they
compensate for variations in TAI. These are defined by yearly
bulletins, and are referred to in TEMPO2 as TT(BIPMyyyy), where
yyyy is the year of the bulletin.

Each bulletin publishes corrections from TAI to TT. It may
revise earlier corrections up to about 10 years back, and it
contains a formula for making predictions past the end of the
data it contains.

This file is pulled from the TEMPO2 repository but is based on
BIPM data and should be unchanging.

|     |     |
|:--- |:--- |
| File | `T2runtime/clock/tai2tt_bipm2003.clk` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/T2runtime/clock/tai2tt_bipm2003.clk> |
| Original download URL | <https://bitbucket.org/psrsoft/tempo2/raw/HEAD/T2runtime/clock/tai2tt_bipm2003.clk> |
| Format | tempo2 |
| Bogus last correction | False |
| Clock file start | 1975-06-26 MJD 42589.0 |
| Clock file end | 2003-07-29 MJD 52849.0 |
| Update interval (days) | inf |
| Last update attempt | 2022-06-13 |
| Last update result | Unchanged |

Log entries from the last few update attempts:
```
2022-06-13 13:55:35.885 - Unchanged
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/T2runtime/clock/tai2tt_bipm2003.clk.log)

Leading comments from clock file:

    #
    # Tie between TAI and TT(BIPM2003), according to
    #  Petit G., A new realization of Terrestrial Time, Proc. 35th PTTI, 2003
    # (http://tycho.usno.navy.mil/ptti/ptti2003/paper29.pdf)
    # from ftp://62.161.69.5/pub/tai/scale/ttbipm.03 , with the following
    # command:
    # awk '{mjd=substr($0,1,5); d=substr($0,15,7); if (mjd > 30000 && mjd < 60000) printf "%.1f %.9f\n", mjd, 32.184+d*1e-6;}' < ttbipm.03 > $TEMPO2/clock/tai2tt_bipm03.clk
    #



All clock corrections:

![plot of all clock corrections](tai2tt_bipm2003.clk.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](tai2tt_bipm2003.clk.short.png "Recent corrections")

