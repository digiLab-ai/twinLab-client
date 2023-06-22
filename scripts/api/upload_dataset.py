import json
import sys

from api import upload_dataset


if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <path/to/dataset.csv> <dataset_id>")
    exit()
filepath = sys.argv[1]
dataset_id = sys.argv[2]

response = upload_dataset(filepath, dataset_id)
print(json.dumps(response, indent=4))
