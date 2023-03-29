# Standard imports
import os

# Project imports
import client as tl


# Inital white space
print()

# Parse command-line arguments
args = tl.get_command_line_args()
server = args.server

# Campaign parameters
params = "campaigns/biscuits/params.json"

# User info
user_info = {
    "group": "digilab",
    "user": os.environ.get("USER"),
    "campaign": "biscuits-python",
}

# Send request and print response
tl.new_campaign(params, user_info, server, verbose=True)
