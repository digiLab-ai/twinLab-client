import json
import sys

import twinlab as tl


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <campaign_id>")
    exit()

campaign_id = sys.argv[1]

_ = tl.status_campaign(campaign_id, verbose=True)
