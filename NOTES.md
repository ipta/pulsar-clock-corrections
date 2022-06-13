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

I'd like to automate the updating but can't really until this runs on a stock
PINT that can easily be pip installed. Currently I'm working off a PR that adds
clock correction file writing.


Observatory contacts
--------------------

- FAST - 
- Effelsberg - Joris Verbiest
- GBT - Ryan Lynch?
- Jodrell Bank - ?
- ...?

How important is it to provide files we don't auto-update? If PINT is to
contain no clock corrections at all, then we need to distribute one for every
observatory PINT knows about. But there are all sorts of other things in the
TEMPO and TEMPO2 distributions. Some are identically zero.

Wishlist
--------

- Comparisons (selected)
- Github action
- Delta value / delta t plots
- Check anomalous points (particularly recent!)
- Check how to tell TEMPO and TEMPO2 which files to actually use if they're taking our clock directories in case they want to choose between (say) TEMPO2's `ao2gps.clk` and the one we generate
    - Tempo - time.dat; files must contain an obscode
    - T2?
- Clock files generated from other sources (can we take advantage of Astropy?)
    - `gps2utc.clk` - BIPM Cicular T, related files, it's a mess; C0 or C0'?
    - `tai2tt_bipm2019.clk` and the like - easy to parse from https://www.bipm.org/en/time-ftp/tt-bipm- but how to handle the profusion of files (including detecting new ones)?
    - `bipmnist.*` - Totally without metadata, better ask what this is but it looks static
    - `leap.sec` - Astropy gets this
    - `ut1.dat` - Astropy's IERS A/B code gets this
    - `utccorr.tot` - Ends 49889 so no updates needed?
    - `utc2tai.clk` - "# UTC TAI" but including what?
    - `utc2ut1.clk` - Should be IERS A/B and thus in Astropy
    - `nist2tai.clk` - 50000-54000 only - maybe we don't have recent data referenced to NIST?
    - `nist2tt_nist.clk` - Supposed to emulate TEMPO?
    - `nist2utc.clk` - Based on Circular T - maybe we don't have recent data referenced to NIST?
- Actual StaticClockFile class for clock files that don't come from anywhere but don't change
    - AO GPS/NIST files that are cut from `time_ao.dat`
    - Maybe not needed?
- Is WSRT data static? If so, can we generate the TEMPO file from the TEMPO2 one? Does the TEMPO2 one cover the whole history?



Questions
---------

- Changing reference time scales: how to handle this? Particularly when converting formats?
    - Older Arecibo clock corrections were not referenced to GPS, but to "NIST" (not quite sure what this means). TEMPO2 separates the two time ranges in the clock corrections files, while the TEMPO clock file simply treats them all the same. 
    - Parkes may have a similar situation.
- Should static clock correction files really have a download URL? Particularly ones where the maintainers of this repository had to change them (e.g. split the converted-from-TEMPO Arecibo clock file based on reference clock)?
    - Conclusion: no.
- Should we try to handle composing time scales to get all TEMPO clock corrections referenced to the same scale? If so, what scale? - TEMPO doesn't distinguish between GPS and other global time scales.
    - PINT uses `include_gps` and `include_bipm` to compensate for this, I think?
