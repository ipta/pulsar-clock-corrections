
## Parkes (TEMPO)

Parkes observatory clock corrections (TEMPO format)

This file is pulled from the TEMPO repository and may not be fully up-to-date.

Note that this file has some clock (non-)correction data for other telescopes
in the same file, distinguished only by observatory code.

|     |     |
|:--- |:--- |
| File | `tempo/clock/time_pks.dat` |
| Authority | temporary |
| URL in repository | <https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/tempo/clock/time_pks.dat> |
| Original download URL | <https://sourceforge.net/p/tempo/tempo/ci/master/tree/clock/time_pks.dat?format=raw> |
| Format | tempo |
| Bogus last correction | True |
| Clock file start | 1979-05-07 MJD 44000.0 |
| Clock file end | 2011-07-03 MJD 55745.8 |
| Update interval (days) | 7 |
| Last update attempt | 2022-06-30 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2022-05-24 17:59:46.903 - Unchanged
2022-05-26 08:30:09.101 - Unchanged
2022-05-26 08:35:06.984 - Unchanged
2022-06-02 11:47:05.758 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-24192-5sncxo_8 in format tempo appears to be out of order
2022-06-09 13:27:38.008 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-10364-7jnkh3d2 in format tempo appears to be out of order
2022-06-16 18:26:27.550 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-16102-wl7_58mt in format tempo appears to be out of order
2022-06-23 20:34:09.487 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1628-9lvowo40 in format tempo appears to be out of order
2022-06-30 20:34:32.763 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1748-evkt486o appears to be out of order
```
[Full log](https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/log/tempo/clock/time_pks.dat.log)

Leading comments from clock file:

    # Irrelevant. -Anne Archibald 2022 May 26
    #  44000.0       0.0               2    ATCA
    #  60000.0       0.0               2    ATCA
    #  44000.0       0.0               H    JBmk2
    #  60000.0       0.0               H    JBmk2
    #  44000.0       0.0               E    MOST
    #  60000.0       0.0               E    MOST



All clock corrections:

![plot of all clock corrections](time_pks.dat.png "All corrections")

Recent clock corrections:

![plot of recent clock corrections](time_pks.dat.short.png "Recent corrections")

