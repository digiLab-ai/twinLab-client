# Standard imports
import os

# Project imports
import twinlab_client as tl


# Inital white space
print()

# Parse command-line arguments
args = tl.get_command_line_args()
server = args.server

# Campaign ID
campaign_id = "biscuits-python"

# Send request and print response
tl.delete_campaign(campaign_id, server, verbose=True)
