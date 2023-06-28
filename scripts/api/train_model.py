import sys
from pprint import pprint

from api import train_model


if len(sys.argv) != 4:
    print(
        f"Usage: python {sys.argv[0]} <path/to/parameters.json> <model_id> <processor>")
    exit()
filepath = sys.argv[1]
model_id = sys.argv[2]
processor = sys.argv[3]

parameters_json = open(filepath, "r").read()
response = train_model(parameters_json, model_id, processor, verbose=True)
pprint(response)
