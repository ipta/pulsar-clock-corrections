from astropy.time import Time
import astropy.utils.data
from datetime import datetime, timedelta

import pint.observatory.clock_file


clockfilebaseurl = "https://www.parkes.atnf.csiro.au/observing/clockfiles/"


def get_mostrecent_pks_url():
    startdate = datetime(Time.now().datetime.year, Time.now().datetime.month, 1)
    currdate = startdate
    while True:
        try:
            filename = f"pks2gps.clk.{currdate.strftime('%Y%m%d')}"
            url = f"{clockfilebaseurl}{filename}"
            f = astropy.utils.data.download_file(url, cache=True)
            break
        except IOError:
            currdate = (currdate + timedelta(days=-1)).replace(day=1)
    return url
