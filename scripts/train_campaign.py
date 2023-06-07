# Standard import
import os
import json

# Project imports
import twinlab as tl

print()  #  Initial white space
filepath = os.path.join("campaigns", "biscuits", "params.json")
campaign_name = "biscuits"
server = tl.get_command_line_args().server
tl.train_campaign(filepath, campaign_name, server=server, verbose=True, debug=True)
