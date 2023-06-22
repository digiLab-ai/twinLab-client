import json

from api import list_datasets


response = list_datasets()
print(json.dumps(response, indent=4))
