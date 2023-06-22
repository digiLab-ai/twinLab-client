import sys

import twinlab as tl


if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <path/to/dataset.csv> <dataset_id>")
    exit()

filepath = sys.argv[1]
dataset_id = sys.argv[2]

tl.upload_dataset(filepath, dataset_id)
