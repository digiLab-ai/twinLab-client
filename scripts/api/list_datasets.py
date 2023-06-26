import json

from api import list_datasets


response = list_datasets(verbose=True)
print(json.dumps(response, indent=4))
