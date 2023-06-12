# Standard import
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = os.path.join("campaigns", "biscuits")
filename = "params.json"
campaign_name = "biscuits"
filepath = os.path.join(directory, filename)
tl.train_campaign(filepath, campaign_name, verbose=True, debug=True)
