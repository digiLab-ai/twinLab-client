# Project imports
import twinlab as tl

print()  #  Initial white space
file = "datasets/bigger.csv"
server = tl.get_command_line_args().server
tl.upload_big_dataset(file, server, verbose=True)
