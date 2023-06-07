# Project imports
import twinlab as tl

print()  #  Initial white space
dataset_name = "biscuits.csv"
server = tl.get_command_line_args().server
tl.query_dataset(dataset_name, server=server, verbose=True, debug=True)
