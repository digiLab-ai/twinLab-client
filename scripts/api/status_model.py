import json
import sys

from api import status_model


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <model_id>")
    exit()
model_id = sys.argv[1]

response = status_model(model_id)
print(json.dumps(response, indent=4))
