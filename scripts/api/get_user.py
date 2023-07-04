from pprint import pprint

from api import get_user

response = get_user(verbose=True)
pprint(response)
