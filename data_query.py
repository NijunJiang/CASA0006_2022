
import pandas as pd
from sodapy import Socrata


# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofchicago.org",
                 'pVPpeQbcdp8k52jNWj7jwRBif',
                "zcfbnji@ucl.ac.uk",
                 "Niyanjun19990913")
where = 'year = 2019 AND primary_type = "BURGLARY"'
# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ijzp-q8t2", limit=100000,where=where)