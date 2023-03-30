# Project imports
import twinlab_client as tl

print()  #  Initial white space
params = "campaigns/biscuits/params.json"
campaign = "biscuits-python"
server = tl.get_command_line_args().server
tl.new_campaign(params, campaign, server, verbose=True)
