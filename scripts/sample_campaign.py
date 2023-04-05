# Project imports
import twinlab_client as tl

print()  #  Initial white space
file = "campaigns/biscuits/eval.csv"
campaign = "biscuits"
server = tl.get_command_line_args().server
df_mean, df_std = tl.sample_campaign(file, campaign, server, verbose=True)
