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

# Load parameters
with open(params_filepath, "r") as f:
    params = json.load(f)

print()  #  Initial white space
server = tl.get_command_line_args().server
tl.upload_dataset(training_filepath, server, verbose=True)
tl.query_dataset(dataset_filename, server, verbose=True)
tl.list_datasets(server, verbose=True)
tl.train_campaign(params, campaign_name, server, verbose=True)
tl.query_campaign(campaign_name, server, verbose=True)
tl.list_campaigns(server, verbose=True)
tl.sample_campaign(eval_filepath, campaign_name, server, verbose=True)
tl.delete_campaign(campaign_name, server, verbose=True)
tl.delete_dataset(dataset_filename, server, verbose=True)
