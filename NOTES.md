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
