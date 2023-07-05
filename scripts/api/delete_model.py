import sys
from pprint import pprint

from api import delete_model


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <model_id>")
    exit()
model_id = sys.argv[1]

response = delete_model(model_id, verbose=True)
pprint(response)
