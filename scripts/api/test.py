import time
from pprint import pprint

import api

dataset_path = "resources/datasets/biscuits.csv"
dataset_id = "biscuits"
params_path = "resources/campaigns/biscuits/params.json"
model_id = "biscuits-model"
predict_path = "resources/campaigns/biscuits/eval.csv"
processor = "cpu"
verbose = True

response = api.get_user(verbose=True)
pprint(response)

response = api.get_versions(verbose=True)
pprint(response)

response = api.list_datasets(verbose=True)
pprint(response)

data_csv = open(dataset_path, "r").read()
response = api.upload_dataset(data_csv, dataset_id, verbose=True)
pprint(response)

response = api.list_datasets(verbose=True)
pprint(response)

response = api.view_dataset(dataset_id, verbose=True)
pprint(response)

response = api.summarise_dataset(dataset_id, verbose=True)
pprint(response)

response = api.list_models(verbose=True)
pprint(response)

parameters_json = open(params_path, "r").read()
response = api.train_model(parameters_json, model_id, processor, verbose=True)
pprint(response)

complete = False  # Wait for job to complete
while not complete:
    status = api.status_model(model_id, verbose=True)
    print("Status:", status)
    complete = status["job_complete"]
    time.sleep(1)

response = api.status_model(model_id, verbose=True)
pprint(response)

response = api.list_models(verbose=True)
pprint(response)

response = api.summarise_model(model_id, verbose=True)
pprint(response)

predict_csv = open(predict_path, "r").read()
response = api.use_model(predict_csv, model_id,
                         "predict", processor, verbose=True)
pprint(response)

response = api.delete_model(model_id, verbose=True)
pprint(response)

response = api.list_models(verbose=True)
pprint(response)

response = api.delete_dataset(dataset_id, verbose=True)
pprint(response)

response = api.list_datasets(verbose=True)
pprint(response)
