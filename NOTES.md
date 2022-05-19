Notes for future use
--------------------

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
