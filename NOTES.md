Notes for future use
====================

PINT includes instructions on getting up-to-date versions of some
non-observatory time information:
https://github.com/nanograv/PINT/blob/master/src/pint/data/runtime/download_data.sh
Just wgets, so easy to arrange from a python script.

GitHub Actions can auto-commit updated files:
https://github.com/marketplace/actions/git-auto-commit This could be combined
with a script run daily (?) to pull in new GBT/BIPM/etc. clock corrections in
order to get steady version-controlled updates pulled in from various sources.

Reporting
---------

github.io publishes markdown files as a web site; we could generate markdown files (including tables) to report the status of the clock corrections and check these in when we run updates.

- State of the clock corrections
    - Start and end date, cadence (typical, recent), last update time, last update status
- Update report
    - Status and error message for each file
- Details about each file
    - Update log, description, related files, plot of corrections?

Clock correction objects
------------------------

- How updates were/are obtained: downloaded, converted, static
    - Authoritative or secondary - did we get it from the observatory or some secondary location? Is this a placeholder?
- Update logs - Failed with reason, unchanged, accepted automatically, accepted manually in spite of validation failure
- Description of file and its origin/update method
- Related files (and how related)
- Canonical order
- Nature (tempo/tempo2 clock correction, other)
- Validation method/settings
- Last major revision (replace clock files older than this regardless)
- How often to check for updates

Observatory contacts
--------------------

- FAST - Weiwei Zhu <zhuww@nao.cas.cn>
- Effelsberg - Joris Verbiest
- GBT - Ryan Lynch?
- Jodrell Bank - ?
- ...?

Wishlist
--------

- Comparisons (selected)
- Details page links to download of actual file
- Github action
- Delta value / delta t plots
- Check anomalous points (particularly recent!)
- Check how to tell TEMPO and TEMPO2 which files to actually use if they're taking our clock directories
    - Tempo - time.dat; files must contain an obscode
    - T2?
