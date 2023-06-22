import json

import twinlab as tl


response = tl.get_user()
print(json.dumps(response, indent=4))
