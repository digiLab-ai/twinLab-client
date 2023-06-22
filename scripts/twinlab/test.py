import time
from pprint import pprint

import twinlab as tl

dataset_path = "resources/datasets/biscuits.csv"
dataset_id = "biscuits"
campaign_path = "resources/campaigns/biscuits/params.json"
campaign_id = "biscuits-campaign"
predict_path = "resources/campaigns/biscuits/eval.csv"

verbose = True
complete = False

_ = tl.get_user(verbose=verbose)
_ = tl.get_versions(verbose=verbose)
_ = tl.list_datasets(verbose=verbose)
tl.upload_dataset(dataset_path, dataset_id, verbose=verbose)
_ = tl.list_datasets()
_ = tl.view_dataset(dataset_id, verbose=verbose)
_ = tl.query_dataset(dataset_id, verbose=verbose)
_ = tl.list_campaigns(verbose=verbose)
tl.train_campaign(campaign_path, campaign_id, verbose=verbose)
while not complete:  # Wait for job to complete
    status = tl.status_campaign(campaign_id)
    complete = status["job_complete"]
    time.sleep(1)
_ = tl.status_campaign(campaign_id, verbose=verbose)
_ = tl.list_campaigns(verbose=verbose)
_ = tl.query_campaign(campaign_id, verbose=verbose)
_ = tl.predict_campaign(predict_path, campaign_id, verbose=verbose)
tl.delete_campaign(campaign_id, verbose=verbose)
_ = tl.list_campaigns()
tl.delete_dataset(dataset_id, verbose=verbose)
_ = tl.list_datasets()
