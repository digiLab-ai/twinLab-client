import json

import twinlab as tl


response = tl.get_versions()
print(json.dumps(response, indent=4))
