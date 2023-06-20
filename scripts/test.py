import time
from pprint import pprint

import twinlab as tl

dataset_path = "resources/datasets/pollution.csv"
dataset_id = "pollution"
campaign_path = "resources/campaigns/pollution/parameters.json"
campaign_id = "pollution-campaign"
predict_path = "resources/campaign/pollution/eval.csv"
processor = "cpu"

response = tl.get_user()
pprint(response)

response = tl.get_versions()
pprint(response)

response = tl.list_datasets()
pprint(response)

response = tl.upload_dataset(dataset_path, dataset_id)
pprint(response)

response = tl.list_datasets()
pprint(response)

response = tl.view_dataset(dataset_id)
pprint(response)

response = tl.query_dataset(dataset_id)
pprint(response)

response = tl.list_campaigns()
pprint(response)

response = tl.train_campaign(campaign_path, campaign_id, processor)
pprint(response)

response = tl.status_campaign(campaign_id)
pprint(response)

# Allow time for the campaign to train
time.sleep(10)

response = tl.status_campaign(campaign_id)
pprint(response)

response = tl.list_campaigns()
pprint(response)

response = tl.query_campaign(campaign_id)
pprint(response)

response = tl.predict_campaign(predict_path, campaign_id, processor)
pprint(response)

response = tl.delete_campaign(campaign_id)
pprint(response)

response = tl.list_campaigns()
pprint(response)

response = tl.delete_dataset(dataset_id)
pprint(response)

response = tl.list_datasets()
pprint(response)
