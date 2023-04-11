# Standard import
import json

# Project imports
import twinlab as tl

print()  #  Initial white space
params_file = "campaigns/biscuits/params.json"
with open(params_file, "r") as f:
    params = json.load(f)
campaign = "biscuits"
server = tl.get_command_line_args().server
tl.train_campaign(params, campaign, server, verbose=True)
