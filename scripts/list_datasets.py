# Project imports
import twinlab as tl

print()  #  Initial white space
server = tl.get_command_line_args().server
datasets = tl.list_datasets(server=server, verbose=True)
print(datasets)
