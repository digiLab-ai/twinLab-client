import json
import sys

from api import train_model


if len(sys.argv) != 4:
    print(
        f"Usage: python {sys.argv[0]} <path/to/parameters.json> <model_id> <processor>")
    exit()
filepath = sys.argv[1]
model_id = sys.argv[2]
processor = sys.argv[3]

response = train_model(filepath, model_id, processor)
print(json.dumps(response, indent=4))
