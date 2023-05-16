# Project imports
import twinlab as tl

print()  #  Initial white space
campaign = "biscuits"
server = tl.get_command_line_args().server
tl.query_campaign(campaign, server=server, verbose=True, debug=True)
