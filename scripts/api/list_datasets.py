from pprint import pprint

from api import list_datasets


response = list_datasets(verbose=True)
pprint(response)
