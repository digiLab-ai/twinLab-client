import sys
from pprint import pprint

from api import process_uploaded_dataset


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <dataset_id>")
    exit()
dataset_id = sys.argv[1]

response = process_uploaded_dataset(dataset_id, verbose=True)
pprint(response)
