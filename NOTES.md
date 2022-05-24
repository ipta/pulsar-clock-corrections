Notes for future use
====================

GBT clock corrections are available from
https://www.gb.nrao.edu/~fghigo/timer/time_gbt.dat, updated approximately
daily, in TEMPO format

PINT includes instructions on getting up-to-date versions of some
non-observatory time information:
https://github.com/nanograv/PINT/blob/master/src/pint/data/runtime/download_data.sh
Just wgets, so easy to arrange from a python script.

GitHub Actions can auto-commit updated files:
https://github.com/marketplace/actions/git-auto-commit This could be combined
with a script run daily (?) to pull in new GBT/BIPM/etc. clock corrections in
order to get steady version-controlled updates pulled in from various sources.

Now contains an initial pass at an auto-downloader - so far only the GBT. The
auto-updater validates the clock corrections - must be a valid clock correction
file (with MJDs in order) and agree with the clock corrections already present
(with the possible exception of a bogus last value) - before updating.

No Github actions machinery yet; that's not helpful if we're not going to live
on Github. But I do want to add a report generator, perhaps making a Markdown
table, that could be used in such a setting; alternatively we might want each
file's update to be a separate action so the success or failure could be
reported through the driver software.

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
