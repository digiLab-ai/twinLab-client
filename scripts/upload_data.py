# Standard imports
import os

# Project imports
import client as tl


# Inital white space
print()

# Parse command-line arguments
args = tl.get_command_line_args()
server = args.server

# Training data
file = "campaigns/biscuits/train.csv"

# User info
user_info = {
    "group": "digilab",
    "user": os.environ.get("USER"),
    "campaign": "biscuits-python",
}

# Send request and print response
tl.upload_data(file, user_info, server, verbose=True)
