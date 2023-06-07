# Project imports
import twinlab as tl

print()  #  Initial white space
campaign_name = "biscuits"
server = tl.get_command_line_args().server
tl.delete_campaign(campaign_name, server=server, verbose=True, debug=True)
