# Standard imports
import os

# Project imports
import twinlab_client as tl


# Inital white space
print()

# Parse command-line arguments
args = tl.get_command_line_args()
server = args.server

# Test data
file = "campaigns/biscuits/eval.csv"

# Campaign ID
campaign_id = "biscuits-python"

# Send request and print response
df_mean, df_std = tl.sample_emulator(file, campaign_id, server, verbose=True)
