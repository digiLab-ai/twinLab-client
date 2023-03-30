# Project imports
import twinlab_client as tl

print()  #  Initial white space
file = "campaigns/biscuits/biscuits.csv"
server = tl.get_command_line_args().server
tl.upload_dataset(file, server, verbose=True)
