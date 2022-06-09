# pulsar-clock-corrections

Distribution point and tools for observatory clock corrections for pulsar timing

In order to precisely time pulsars, we need to know precisely when the data was
taken. Most observatories maintain their own clocks but keep track of how these
clocks deviate from International Atomic Time, usually by way of GPS. Thus to
accurately work with data from these observatories, pulsar timing software must
have access to these clock corrections. Because they are records of the
behaviour of physical clocks, these corrections cannot be predicted and
therefore one must obtain a list of clock corrections updated since the last
data point one wishes to analyze was taken. 

This package is designed to address the problem of distributing these
up-to-date clock correction files.

The intention is that this package be useful to users of the three major pieces
of pulsar timing software: TEMPO, TEMPO2, and PINT.

This package includes both the repository itself (with detailed logs of the
updating process) and some tools for maintaining it. The maintenance tools
use Python, Astropy, and PINT, but most users should have no need to run them.

To browse the repository, and for instructions on how to use the files in it,
please visit https://ipta.github.io/pulsar-clock-corrections/
