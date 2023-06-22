import json

from api import get_user


response = get_user()
print(json.dumps(response, indent=4))
