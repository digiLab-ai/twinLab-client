import json

from api import list_models


response = list_models()
print(json.dumps(response, indent=4))
