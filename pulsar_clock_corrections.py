import numpy as np
import os
from pint.observatory.clock_file import ClockFile
from astropy.utils.data import download_file
from pathlib import Path

def base_location():
    return Path(__file__).parent

def list_candidate_clock_files():
    return sorted(base_location().glob("tempo/clock/time*_*.dat")) + sorted(base_location().glob("T2runtime/clock/*2*.clk"))

class ValidationError(RuntimeError):
    pass


class ClockFileUpdater:
    def __init__(self, filename, download_url=None, format="tempo", bogus_last_entry=False, obscode=None):
        self.filename = filename
        self.filepath = base_location()/self.filename
        self.format = format
        self.bogus_last_entry = bogus_last_entry
        self.download_url = download_url
        self.obscode = obscode

    def get(self, cache=False):
        return download_file(self.download_url, cache=cache)

    def validate(self, old_file, new_file):
        old = ClockFile.read(old_file, format=self.format, bogus_last_entry=self.bogus_last_entry, obscode=self.obscode)
        new = ClockFile.read(new_file, format=self.format, bogus_last_entry=self.bogus_last_entry, obscode=self.obscode)
        d = old.time != new.time[:len(old.time)]
        if np.any(d):
            raise ValidationError(f"New version of {old_file} MJDs differ from old version where they overlap in {np.sum(d)} places")
        d = old.clock != new.clock[:len(old.clock)]
        if np.any(d):
            raise ValidationError(f"New version of {old_file} clock corrections differ from old version where they overlap in {np.sum(d)} places")

    def try_update(self, cache=False):
        try:
            f = self.get(cache=cache)
        except IOError as e:
            return False, f"Failed to download {self.filename}: {e}"
        old_contents = self.filepath.read_text()
        new_contents = Path(f).read_text()
        if old_contents == new_contents:
            return True, f"Downloaded file for {self.filename} is unchanged"
        try:
            self.validate(base_location()/self.filename, f)
        except ValidationError as e:
            return False, f"Downloaded file for {self.filename} couldn't be validated: {e}"
        self.filepath.write_text(new_contents)
        return True, f"Updated {self.filename}"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.filename}")'

updaters = [
    ClockFileUpdater("tempo/clock/time3_gbt.dat", download_url="https://www.gb.nrao.edu/~fghigo/timer/time_gbt.dat", format="tempo", obscode="3")
]


