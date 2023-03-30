# Project imports
import twinlab_client as tl

print()  #  Initial white space
file = "campaigns/biscuits/eval.csv"
campaign = "biscuits-python"
server = tl.get_command_line_args().server
df_mean, df_std = tl.sample_emulator(file, campaign, server, verbose=True)
