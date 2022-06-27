#!/usr/bin/env python
"""Download up-to-date clock corrections to $TEMPO or $TEMPO2.

This script should run on any system with python3 - it should *not* require
PINT or astropy or any particular machinery that doesn't come with python.
It should be simple to run, and it should result in downloaded clock files
from the global repository being available for use.
"""

import os
import logging
import tempfile
from pathlib import Path
from urllib.request import urlopen

log = logging.getLogger(__name__)

public_repo_url_raw = (
    "https://raw.githubusercontent.com/ipta/pulsar-clock-corrections/main/"
)


def download_corrections():
    """Download clock corrections to a repository."""  # FIXME: be able to do this in a directory that will stick around
    # for troubleshooting; mostly means make appropriate subdirectories
    index_url = public_repo_url_raw + "index.txt"
    log.info(f"Downloading index from {index_url}")
    index = urlopen(index_url).read().decode("utf-8")
    for line in index.split("\n"):
        if line.strip().startswith("#") or not line.strip():
            continue
        filename, _, _ = line.split()
        # FIXME: skip if wrong format
        # FIXME: ensure it goes in the right place (strip leading path component)
        filename = Path(filename)
        if filename.parts[0] == "tempo":
            if "TEMPO" in os.environ:
                local_filename = Path(os.environ["TEMPO"]) / Path(*filename.parts[1:])
            else:
                log.info(f"Skipping {filename} because $TEMPO not set")
                continue
        elif filename.parts[0] == "T2runtime":
            if "TEMPO2" in os.environ:
                local_filename = Path(os.environ["TEMPO2"]) / Path(*filename.parts[1:])
            else:
                log.info(f"Skipping {filename} because $TEMPO2 not set")
                continue
        else:
            log.info(f"Skipping {filename} because format not recognized")
            continue
        file_url = public_repo_url_raw + str(filename)
        log.info(f"Downloading {filename} from {file_url} to {local_filename}")
        # FIXME: make sure the file was successfully downloaded before writing anything
        contents = urlopen(file_url).read().decode("utf-8")
        if local_filename.exists():
            old_contents = local_filename.read_text()
            lc = len(contents.split("\n"))
            loc = len(old_contents.split("\n"))
            if old_contents == contents:
                log.info(f"Not updating {filename} as contents are unchanged")
            else:
                log.info(
                    f"New version of {filename} has {lc} lines and old version has {loc} lines, updating"
                )
                local_filename.write_text(contents)
        else:
            local_filename.parent.mkdir(parents=True, exist_ok=True)
            log.info(f"New file {filename}")
            local_filename.write_text(contents)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    download_corrections()
