from glob import glob
import os

def list_candidate_clock_files():
    return sorted(glob("tempo/clock/time*_*.dat")) + sorted(glob("T2runtime/clock/*2*.clk"))

