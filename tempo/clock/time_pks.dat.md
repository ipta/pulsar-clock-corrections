
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
| Last update attempt | 2025-02-12 |
| Last update result | Validation failed |

Log entries from the last few update attempts:
```
2024-12-11 20:40:40.481 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2157-57ooi6g4 appears to be out of order: 49959.0 > 49958.0
2024-12-18 20:39:24.379 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2274-q5yfgh14 appears to be out of order: 49959.0 > 49958.0
2024-12-25 20:35:15.566 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2307-uzx6wu0r appears to be out of order: 49959.0 > 49958.0
2025-01-01 20:35:37.359 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2322-zqzvwthm appears to be out of order: 49959.0 > 49958.0
2025-01-08 20:36:54.237 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2276-gpk3q2dj appears to be out of order: 49959.0 > 49958.0
2025-01-15 20:35:03.801 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2348-0794xif6 appears to be out of order: 49959.0 > 49958.0
2025-01-22 20:35:06.602 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2304-98v3yima appears to be out of order: 49959.0 > 49958.0
2025-01-29 20:35:46.314 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2314-e3p7x51_ appears to be out of order: 49959.0 > 49958.0
2025-02-05 20:37:08.242 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2343-ovr9scze appears to be out of order: 49959.0 > 49958.0
2025-02-12 20:36:34.000 - Validation failed: Unable to read new version of tempo/clock/time_pks.dat: Clock file /tmp/astropy-download-2294-sgs73xt5 appears to be out of order: 49959.0 > 49958.0
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

