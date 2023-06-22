import time
import json
from pprint import pprint

import api

dataset_path = "resources/datasets/biscuits.csv"
dataset_id = "biscuits"
params_path = "resources/campaigns/biscuits/params.json"
model_id = "biscuits-model"
predict_path = "resources/campaigns/biscuits/eval.csv"
processor = "cpu"

response = api.get_user()
pprint(response)

response = api.get_versions()
pprint(response)

response = api.list_datasets()
pprint(response)

data_csv = open(dataset_path, "r").read()
response = api.upload_dataset(data_csv, dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)

response = api.view_dataset(dataset_id)
pprint(response)

response = api.summarise_dataset(dataset_id)
pprint(response)

response = api.list_models()
pprint(response)

parameters_json = open(params_path, "r").read()
response = api.train_model(parameters_json, model_id, processor)
pprint(response)

complete = False  # Wait for job to complete
while not complete:
    status = api.status_model(model_id)
    complete = status["job_complete"]
    time.sleep(1)

response = api.status_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.summarise_model(model_id)
pprint(response)

predict_csv = open(predict_path, "r").read()
response = api.use_model(predict_csv, model_id, "predict", processor)
pprint(response)

response = api.delete_model(model_id)
pprint(response)

response = api.list_models()
pprint(response)

response = api.delete_dataset(dataset_id)
pprint(response)

response = api.list_datasets()
pprint(response)
