import json

from api import get_versions


response = get_versions()
print(json.dumps(response, indent=4))
