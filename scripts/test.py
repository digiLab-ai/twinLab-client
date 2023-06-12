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
tl.upload_dataset(training_filepath,
                  verbose=verbose, debug=debug)
tl.query_dataset(dataset_name, verbose=verbose, debug=debug)
tl.list_datasets(verbose=verbose, debug=debug)
tl.train_campaign(params_filepath, campaign_name,
                  verbose=verbose, debug=debug)
tl.query_campaign(campaign_name, verbose=verbose, debug=debug)
tl.list_campaigns(verbose=verbose, debug=debug)
tl.predict_campaign(eval_filepath, campaign_name,
                    verbose=verbose, debug=debug)
tl.delete_campaign(campaign_name, verbose=verbose, debug=debug)
tl.delete_dataset(dataset_name,
                  verbose=verbose, debug=debug)
