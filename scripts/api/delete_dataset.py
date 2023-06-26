import json
import sys

from api import delete_dataset


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <dataset_id>")
    exit()
dataset_id = sys.argv[1]

response = delete_dataset(dataset_id, verbose=True)
print(json.dumps(response, indent=4))
