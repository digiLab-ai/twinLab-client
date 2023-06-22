import json
import sys

import twinlab as tl

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <dataset_id>")
    exit()

dataset_id = sys.argv[1]

response = tl.query_dataset(dataset_id)
print(json.dumps(response, indent=4))
