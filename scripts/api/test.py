import time
from pprint import pprint

import api

WAIT_TIME = 10  # Time for training to definitely complete [s]

dataset_path = "resources/datasets/biscuits.csv"
dataset_id = "biscuits"
model_path = "resources/campaigns/biscuits/params.json"
model_id = "biscuits-model"
predict_path = "resources/campaigns/biscuits/eval.csv"
processor = "cpu"

response = api.get_user()
pprint(response)

response = api.get_versions()
pprint(response)

response = api.list_datasets()
pprint(response)

response = api.upload_dataset(dataset_path, dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)

response = api.view_dataset(dataset_id)
pprint(response)

response = api.summarise_dataset(dataset_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.train_model(model_path, model_id, processor)
pprint(response)

response = api.status_model(model_id)
pprint(response)

# Allow time for the model to train
print(f"Waiting {WAIT_TIME}s for model to train...")
time.sleep(WAIT_TIME)

response = api.status_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.summarise_model(model_id)
pprint(response)

response = api.use_model(
    predict_path, model_id, "predict", processor)
pprint(response)

response = api.delete_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.delete_dataset(dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)
