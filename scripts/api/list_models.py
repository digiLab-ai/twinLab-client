from pprint import pprint

from api import list_models


response = list_models(verbose=True)
pprint(response)
