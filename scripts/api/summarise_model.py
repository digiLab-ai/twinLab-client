import json
import sys

from api import summarise_model

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <model_id>")
    exit()
model_id = sys.argv[1]

response = summarise_model(model_id, verbose=True)
print(json.dumps(response, indent=4))
