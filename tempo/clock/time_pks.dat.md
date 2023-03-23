
## Parkes (TEMPO)

Parkes observatory clock corrections (TEMPO format)

This file is pulled from the TEMPO repository and may not be fully
up-to-date.

Note that this file has some clock (non-)correction data for other
telescopes in the same file, distinguished only by observatory code.

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
| Last update attempt | 2023-03-23 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2023-01-19 20:29:27.268 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1776-mnk33jo5 appears to be out of order
2023-01-26 20:27:52.361 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1727-mtkw35or appears to be out of order
2023-02-02 20:29:10.866 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1774-g45b96pq appears to be out of order
2023-02-09 20:30:00.469 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1673-rxt_dgw7 appears to be out of order
2023-02-16 20:29:21.076 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1683-dap3d7f_ appears to be out of order
2023-02-23 20:30:38.067 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1718-yry0f46l appears to be out of order
2023-03-02 20:30:48.526 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1706-_i5l6zu0 appears to be out of order
2023-03-09 20:31:05.060 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1730-tvhmpzn8 appears to be out of order
2023-03-16 20:29:09.497 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1726-u716fwx7 appears to be out of order
2023-03-23 20:27:47.249 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1727-75z30o3m appears to be out of order
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

