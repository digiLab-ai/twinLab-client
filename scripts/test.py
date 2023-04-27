# Standard imports
import json

# Project imports
import twinlab as tl

# Parameters
dataset_dir = "datasets"
dataset = "biscuits.csv"
campaign_dir = "campaigns/biscuits"
training_file = dataset_dir+"/"+dataset
params_file = campaign_dir+"/params.json"
eval_file = campaign_dir+"/eval.csv"
campaign = "biscuits"

# Load parameters
with open(params_file, "r") as f:
    params = json.load(f)

print()  #  Initial white space
server = tl.get_command_line_args().server
tl.upload_dataset(training_file, server, verbose=True)
tl.query_dataset(dataset, server, verbose=True)
tl.list_datasets(server, verbose=True)
tl.train_campaign(params, campaign, server, verbose=True)
tl.query_campaign(campaign, server, verbose=True)
tl.list_campaigns(server, verbose=True)
tl.sample_campaign(eval_file, campaign, server, verbose=True)
tl.delete_campaign(campaign, server, verbose=True)
tl.delete_dataset(dataset, server, verbose=True)
