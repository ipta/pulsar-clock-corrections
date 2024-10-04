
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
| Last update attempt | 2024-10-04 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2024-08-02 20:31:15.123 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1884-prw9g2tg appears to be out of order: 49959.0 > 49958.0
2024-08-09 20:31:11.284 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1813-swwbjeka appears to be out of order: 49959.0 > 49958.0
2024-08-16 20:31:04.370 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1819-bg24jb3b appears to be out of order: 49959.0 > 49958.0
2024-08-23 20:30:59.058 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1777-zxlnpoxz appears to be out of order: 49959.0 > 49958.0
2024-08-30 20:32:33.550 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1806-7nmpd07j appears to be out of order: 49959.0 > 49958.0
2024-09-06 20:31:32.232 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1810-y5xp7me4 appears to be out of order: 49959.0 > 49958.0
2024-09-13 20:32:08.063 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1899-ep23bl8p appears to be out of order: 49959.0 > 49958.0
2024-09-20 20:33:31.784 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1893-m35dbe__ appears to be out of order: 49959.0 > 49958.0
2024-09-27 20:33:24.548 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1803-aho2ayns appears to be out of order: 49959.0 > 49958.0
2024-10-04 20:33:16.722 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-1844-zxupk919 appears to be out of order: 49959.0 > 49958.0
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

