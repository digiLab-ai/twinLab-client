# Standard imports
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = os.path.join("campaigns", "biscuits")
filename = "eval.csv"
campaign_name = "biscuits"
filepath = os.path.join(directory, filename)
server = tl.get_command_line_args().server
df_mean, df_std = tl.predict_campaign(
    filepath, campaign_name, server=server, verbose=True, debug=True)
