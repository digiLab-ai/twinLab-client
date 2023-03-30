# Standard imports
import os

# Project imports
import twinlab_client as tl


# Inital white space
print()

# Parse command-line arguments
args = tl.get_command_line_args()
server = args.server

# Training data
file = "campaigns/biscuits/train.csv"

# Campaign ID
campaign_id = "biscuits-python"

# Send request and print response
tl.upload_data(file, campaign_id, server, verbose=True)
