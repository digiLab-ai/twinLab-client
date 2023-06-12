# Standard imports
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = "datasets"
filename = "biscuits.csv"
filepath = os.path.join(directory, filename)
server = tl.get_command_line_args().server
tl.upload_dataset(filepath, server=server, verbose=True, debug=True)
