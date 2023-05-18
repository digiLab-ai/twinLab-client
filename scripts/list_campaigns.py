# Project imports
import twinlab as tl

print()  #  Initial white space
server = tl.get_command_line_args().server
campaigns = tl.list_campaigns(server=server, verbose=True, debug=True)
print(campaigns)
