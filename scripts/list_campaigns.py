# Project imports
import twinlab as tl

print()  #  Initial white space
server = tl.get_command_line_args().server
campaigns = tl.list_campaigns(server, verbose=True)
print(campaigns)
