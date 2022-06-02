## Using these clock corrections

This repository contains clock files in TEMPO and TEMPO2 format, laid out in
directories that mimic the clock correction directories of TEMPO and TEMPO2.
They are stored in a git repository on Github, so their full histories are
available, should there be any question of problematic changes. There are a
number of ways to make these files available to your pulsar timing software,
but I will recommend a specific simple approach.

### TEMPO and TEMPO2

The script `download-clock-corrections.py` downloads all clock files into the
directories pointed to by your `$TEMPO` and `$TEMPO2` environment variables. Simply
running the script should immediately replace (!) all clock files with the
versions stored in the repository. You will get reports on the update process -
which files are new, unchanged, or changed and therefore have been updated.

If you want more control over the process, you can set `$TEMPO` and `$TEMPO2` to somewhere inoffensive:

```
$ export TEMPO=/tmp/tempo
$ export TEMPO2=/tmp/tempo2
$ python download-clock-corrections.py
Downloading index from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/index.txt
Downloading T2runtime/clock/gps2utc.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/gps2utc.clk to /tmp/tempo2/clock/gps2utc.clk
New file T2runtime/clock/gps2utc.clk
Downloading tempo/clock/time3_gbt.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time3_gbt.dat to /tmp/tempo/clock/time3_gbt.dat
New file tempo/clock/time3_gbt.dat
Downloading T2runtime/clock/gbt2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/gbt2gps.clk to /tmp/tempo2/clock/gbt2gps.clk
New file T2runtime/clock/gbt2gps.clk
Downloading T2runtime/clock/gbt2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/gbt2gps.clk to /tmp/tempo2/clock/gbt2gps.clk
Not updating T2runtime/clock/gbt2gps.clk as contents are unchanged
Downloading tempo/clock/time_jb.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_jb.dat to /tmp/tempo/clock/time_jb.dat
New file tempo/clock/time_jb.dat
Downloading T2runtime/clock/jb2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/jb2gps.clk to /tmp/tempo2/clock/jb2gps.clk
New file T2runtime/clock/jb2gps.clk
Downloading tempo/clock/time_ao.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_ao.dat to /tmp/tempo/clock/time_ao.dat
New file tempo/clock/time_ao.dat
Downloading T2runtime/clock/ao2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/ao2gps.clk to /tmp/tempo2/clock/ao2gps.clk
New file T2runtime/clock/ao2gps.clk
Downloading T2runtime/clock/ao2gps_tempo2.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/ao2gps_tempo2.clk to /tmp/tempo2/clock/ao2gps_tempo2.clk
New file T2runtime/clock/ao2gps_tempo2.clk
Downloading T2runtime/clock/ao2nist.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/ao2nist.clk to /tmp/tempo2/clock/ao2nist.clk
New file T2runtime/clock/ao2nist.clk
Downloading tempo/clock/time_gb140.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_gb140.dat to /tmp/tempo/clock/time_gb140.dat
New file tempo/clock/time_gb140.dat
Downloading tempo/clock/time_gb853.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_gb853.dat to /tmp/tempo/clock/time_gb853.dat
New file tempo/clock/time_gb853.dat
Downloading tempo/clock/time_vla.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_vla.dat to /tmp/tempo/clock/time_vla.dat
New file tempo/clock/time_vla.dat
Downloading T2runtime/clock/vla2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/vla2gps.clk to /tmp/tempo2/clock/vla2gps.clk
New file T2runtime/clock/vla2gps.clk
Downloading T2runtime/clock/vla2nist.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/vla2nist.clk to /tmp/tempo2/clock/vla2nist.clk
New file T2runtime/clock/vla2nist.clk
Downloading tempo/clock/time_fast.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_fast.dat to /tmp/tempo/clock/time_fast.dat
New file tempo/clock/time_fast.dat
Downloading T2runtime/clock/wsrt2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/wsrt2gps.clk to /tmp/tempo2/clock/wsrt2gps.clk
New file T2runtime/clock/wsrt2gps.clk
Downloading tempo/clock/time_wsrt.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_wsrt.dat to /tmp/tempo/clock/time_wsrt.dat
New file tempo/clock/time_wsrt.dat
Downloading T2runtime/clock/pks2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/pks2gps.clk to /tmp/tempo2/clock/pks2gps.clk
New file T2runtime/clock/pks2gps.clk
Downloading tempo/clock/time_pks.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_pks.dat to /tmp/tempo/clock/time_pks.dat
New file tempo/clock/time_pks.dat
Downloading T2runtime/clock/srt2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/srt2gps.clk to /tmp/tempo2/clock/srt2gps.clk
New file T2runtime/clock/srt2gps.clk
Downloading T2runtime/clock/eff2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/eff2gps.clk to /tmp/tempo2/clock/eff2gps.clk
New file T2runtime/clock/eff2gps.clk
Downloading T2runtime/clock/effix2gps.clk from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/T2runtime/clock/effix2gps.clk to /tmp/tempo2/clock/effix2gps.clk
New file T2runtime/clock/effix2gps.clk
Downloading tempo/clock/time_nuppi.dat from https://raw.githubusercontent.com/nanograv/pulsar-clock-corrections/main/tempo/clock/time_nuppi.dat to /tmp/tempo/clock/time_nuppi.dat
New file tempo/clock/time_nuppi.dat
```

Now your new clock corrections are all available in the locations you requested
and you can check their contents and copy them over to the appropriate places.

If you want even more control over the clock corrections, for example access to their history and the opportunity to suggest changes, you can `git clone` the repository:

```
$ git clone https://github.com/nanograv/pulsar-clock-corrections.git
```

### PINT

If you use PINT, you are probably aware that it is in active development. At
the moment, the best way to get up-to-date clock corrections is to ask the
maintainers to update the clock corrections in PINT. But as of 2022 June 2,
there is a pull request under active development to make PINT request
up-to-date clock corrections directly from the repository. Long-term, the
intention of the PINT developers is that you need not do anything to obtain
up-to-date clock corrections from this repository.
