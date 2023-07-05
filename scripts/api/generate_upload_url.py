import sys
from pprint import pprint

from api import generate_upload_url


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <dataset_id>")
    exit()
dataset_id = sys.argv[1]

response = generate_upload_url(dataset_id, verbose=True)
pprint(response)
