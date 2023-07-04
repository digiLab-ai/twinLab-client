import json
import sys

import twinlab as tl

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <path/to/dataset.csv> <campaign_id>")
    exit()

filepath = sys.argv[1]
campaign_id = sys.argv[2]

_ = tl.predict_campaign(filepath, campaign_id, verbose=True)
