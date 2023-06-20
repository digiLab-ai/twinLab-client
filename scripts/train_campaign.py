import sys

import twinlab as tl


if len(sys.argv) != 5:
    print(
        f"Usage: python {sys.argv[0]} <path/to/inputs.csv> <campaign_id> <method> <processor>")
    exit()

filepath = sys.argv[1]
campaign_id = sys.argv[2]
method = sys.argv[3]
processor = sys.argv[4]

response = tl.use_campaign(filepath, campaign_id, method, processor)
print(response)
