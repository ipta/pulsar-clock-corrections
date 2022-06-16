import pulsar_clock_corrections
import pint.logging
import argparse

def do_all_updates(directory):
    pulsar_clock_corrections.try_all_updates()
    p = pulsar_clock_corrections.PagesUpdater(directory)
    p.update_summary()
    p.generate_details_pages()
    pulsar_clock_corrections.generate_index_txt()

if __name__=='__main__':
    # setup logging
    pint.logging.setup(level="INFO")
    parser = argparse.ArgumentParser(description="Update clock corrections and report results.")
    parser.add_argument("--gh-pages", default="../gh-pages", help="Directory to write status updates to")
    args = parser.parse_args()
    # Check out the gh-pages branch somewhere
    do_all_updates(args.gh_pages)
    # Check in changes
