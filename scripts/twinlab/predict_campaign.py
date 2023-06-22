import json
import sys

import twinlab as tl

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <path/to/dataset.csv> <campaign_id>")
    exit()

filepath = sys.argv[1]
campaign_id = sys.argv[2]

df_mean, df_std = tl.predict_campaign(filepath, campaign_id)
print(df_mean)
print(df_std)
# print(json.dumps(response, indent=4))
