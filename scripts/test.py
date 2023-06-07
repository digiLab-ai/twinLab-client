# Standard imports
import os

# Project imports
import twinlab as tl

# Parameters
dataset_directory = "datasets"
dataset_filename = "biscuits.csv"
dataset_name = dataset_filename
campaign_directory = os.path.join("campaigns", "biscuits")
training_filepath = os.path.join(dataset_directory, dataset_filename)
params_filepath = os.path.join(campaign_directory, "params.json")
eval_filepath = os.path.join(campaign_directory, "eval.csv")
campaign_name = "biscuits"
verbose = True
debug = False

print()  #  Initial white space
server = tl.get_command_line_args().server
tl.upload_dataset(training_filepath, server=server,
                  verbose=verbose, debug=debug)
tl.query_dataset(dataset_name, server=server, verbose=verbose, debug=debug)
tl.list_datasets(server=server, verbose=verbose, debug=debug)
tl.train_campaign(params_filepath, campaign_name, server=server,
                  verbose=verbose, debug=debug)
tl.query_campaign(campaign_name, server=server, verbose=verbose, debug=debug)
tl.list_campaigns(server=server, verbose=verbose, debug=debug)
tl.predict_campaign(eval_filepath, campaign_name,
                    server=server, verbose=verbose, debug=debug)
tl.delete_campaign(campaign_name, server=server, verbose=verbose, debug=debug)
tl.delete_dataset(dataset_name, server=server,
                  verbose=verbose, debug=debug)
