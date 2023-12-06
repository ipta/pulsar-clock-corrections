import argparse

import pint.logging

import pulsar_clock_corrections


def do_all_updates(directory, respect_interval=True, files=None, force=False):
    if files is None:
        files = []
    if not files:
        pulsar_clock_corrections.try_all_updates(respect_interval=respect_interval)
    else:
        for f in files:
            u = pulsar_clock_corrections.get_updater(f)
            u.try_update(respect_interval=respect_interval, force=force)
            print(f"{u.short_description:20} {u.last_log_entry.strip()}")

    p = pulsar_clock_corrections.PagesUpdater(directory)
    p.update_summary()
    p.generate_details_pages()
    pulsar_clock_corrections.generate_index_txt()


if __name__ == "__main__":
    # setup logging
    pint.logging.setup(level="INFO")
    parser = argparse.ArgumentParser(
        description="Update clock corrections and report results."
    )
    parser.add_argument(
        "--gh-pages", default="../gh-pages", help="Directory to write status updates to"
    )
    parser.add_argument(
        "--no-respect-interval",
        action="store_true",
        help="Disregard update intervals and force a retry",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force update even if it disagrees with a previous version",
    )
    parser.add_argument("--file", action="append", help="Update only this file")
    args = parser.parse_args()
    # Check out the gh-pages branch somewhere
    do_all_updates(
        args.gh_pages,
        respect_interval=not args.no_respect_interval,
        files=args.file,
        force=args.force,
    )
    # Check in changes
