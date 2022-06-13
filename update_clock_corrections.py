import pulsar_clock_corrections
import pint.logging

def do_all_updates(directory):
    pulsar_clock_corrections.try_all_updates()
    p = pulsar_clock_corrections.PagesUpdater("../gh-pages")
    p.update_summary()
    p.generate_details_pages()
    pulsar_clock_corrections.generate_index_txt()

if __name__=='__main__':
    # setup logging
    pint.logging.setup(level="INFO")
    # Check out the gh-pages branch somewhere
    do_all_updates("../gh-pages")
    # Check in changes
