# Standard import
import os
import json

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = os.path.join("campaigns", "biscuits")
filename = "params.json"
campaign_name = "biscuits"
filepath = os.path.join(directory, filename)
server = tl.get_command_line_args().server
tl.train_campaign(filepath, campaign_name, server=server,
                  verbose=True, debug=True)
