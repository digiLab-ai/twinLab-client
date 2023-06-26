import json

from api import get_user


response = get_user(verbose=True)
print(json.dumps(response, indent=4))
