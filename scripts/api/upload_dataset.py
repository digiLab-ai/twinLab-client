import sys
from pprint import pprint

from api import upload_dataset


if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <path/to/dataset.csv> <dataset_id>")
    exit()
filepath = sys.argv[1]
dataset_id = sys.argv[2]

data_csv = open(filepath, "r").read()
response = upload_dataset(data_csv, dataset_id, verbose=True)
pprint(response)
