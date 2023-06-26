import sys

from api import view_dataset


if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <dataset_id>")
    exit()
dataset_id = sys.argv[1]

response = view_dataset(dataset_id, verbose=True)
print(response)
