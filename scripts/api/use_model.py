import sys
from pprint import pprint

from api import use_model


if len(sys.argv) != 5:
    print(
        f"Usage: python {sys.argv[0]} <path/to/inputs.csv> <model_id> <method> <processor>")
    exit()
filepath = sys.argv[1]
model_id = sys.argv[2]
method = sys.argv[3]
processor = sys.argv[4]

eval_csv = open(filepath, "r").read()
response = use_model(eval_csv, model_id, method, processor, verbose=True)
pprint(response)
