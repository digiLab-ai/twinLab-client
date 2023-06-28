from pprint import pprint

from api import get_versions


response = get_versions(verbose=True)
pprint(response)
