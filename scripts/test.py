# Standard imports
import json

# Project imports
import twinlab as tl

# Parameters
dataset_directory = "datasets"
dataset_filename = "biscuits.csv"
campaign_directory = "campaigns/biscuits"
training_filepath = dataset_directory+"/"+dataset_filename
params_filepath = campaign_directory+"/params.json"
eval_filepath = campaign_directory+"/eval.csv"
campaign_name = "biscuits"
verbose = True
debug = False

# Load parameters
with open(params_filepath, "r") as f:
    params = json.load(f)

print()  #  Initial white space
server = tl.get_command_line_args().server
tl.upload_dataset(training_filepath, server=server,
                  verbose=verbose, debug=debug)
tl.query_dataset(dataset_filename, server=server, verbose=verbose, debug=debug)
tl.list_datasets(server=server, verbose=verbose, debug=debug)
tl.train_campaign(params, campaign_name, server=server,
                  verbose=verbose, debug=debug)
tl.query_campaign(campaign_name, server=server, verbose=verbose, debug=debug)
tl.list_campaigns(server=server, verbose=verbose, debug=debug)
tl.predict_campaign(eval_filepath, campaign_name,
                    server=server, verbose=verbose, debug=debug)
tl.delete_campaign(campaign_name, server=server, verbose=verbose, debug=debug)
tl.delete_dataset(dataset_filename, server=server,
                  verbose=verbose, debug=debug)
