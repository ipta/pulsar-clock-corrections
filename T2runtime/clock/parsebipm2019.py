#!usr/bin/env python
# This builds the tai2tt_bipm2019.clk file from the TTBIPM.2019 file distributed by the BIPM
# Paul Ray, 2020 August 11
#
# This is specific to BIPM 2019 since it implements the extrapolation formula.  
# For other epochs, make sure to update the extrapolation based on the formula shown in the officil
# file header.

import astropy
import numpy as np

# To use, first download latest BIPM file like this:
# curl -O ftp://ftp2.bipm.org/pub/tai/ttbipm/TTBIPM.2019
# Then comment out (with #) or delete all the header lines
# Then just run parsebipy2019.py
# It will create (or overwrite) tai2tt_bipm2019.clk

# Read BIPM file
mjd,eal,dtai = np.loadtxt('TTBIPM.2019',unpack=True,comments="#")

# Create output file
outf = open("tai2tt_bipm2019.clk","w")

# Write comment header
print("# TAI to TT(BIPM2019), with BIPM recommended extrapolation",file=outf)
print("# Created by parsebipm2019.py",file=outf)

# Write out official values
tt = dtai*1.0E-6 + 32.184
[print("{:.0f}  {:.10f}".format(m,t),file=outf) for m,t in zip(mjd,tt)]

# Now add ~1000 days of extrapolation, according to this formula from the file header:
# Until the next realization, users can extend TT(BIPM19) after MJD 58839 as
# TT(BIPM19) = TAI + 32.184 s + 27680.0 ns - 0.02x(MJD-58839) ns 
extrapmjd = mjd[-1] + 10.0*(1+np.arange(104))
extraptt = 32.184 + 27680*1.0E-9 - 0.02*1E-9*(extrapmjd-58839)
[print("{:.0f}  {:.10f}".format(m,t),file=outf) for m,t in zip(extrapmjd,extraptt)]
