import time
from pprint import pprint

import twinlab as tl

dataset_path = "resources/datasets/biscuits.csv"
dataset_id = "biscuits"
model_path = "resources/campaigns/biscuits/params.json"
model_id = "biscuits-model"
predict_path = "resources/campaigns/biscuits/eval.csv"

verbose = True

_ = tl.get_user(verbose=verbose)
_ = tl.get_versions(verbose=verbose)
_ = tl.list_datasets(verbose=verbose)
tl.upload_dataset(dataset_path, dataset_id, verbose=verbose)
_ = tl.list_datasets()
_ = tl.view_dataset(dataset_id, verbose=verbose)
_ = tl.query_dataset(dataset_id, verbose=verbose)
_ = tl.list_campaigns(verbose=verbose)
tl.train_campaign(model_path, model_id, verbose=verbose)
_ = tl.status_campaign(model_id, verbose=verbose)
time.sleep(10)  # Allow time for the campaign to train
_ = tl.status_campaign(model_id, verbose=verbose)
_ = tl.list_campaigns(verbose=verbose)
_ = tl.query_campaign(model_id, verbose=verbose)
_ = tl.predict_campaign(predict_path, model_id, verbose=verbose)
tl.delete_campaign(model_id, verbose=verbose)
_ = tl.list_campaigns()
tl.delete_dataset(dataset_id, verbose=verbose)
_ = tl.list_datasets()
