# Third-party imports
from pydantic import BaseSettings

# Project imports
from ._version import __version__
from . import api


class Environment(BaseSettings):
    TWINLAB_SERVER: str
    TWINLAB_HOST: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()

twinlab_user = api.get_user()["username"]

print()
print("         === TwinLab Client Initialisation ===")
print(f"         Version  : {__version__}")
print(f"         User     : {twinlab_user}")
print(f"         Host     : {ENV.TWINLAB_HOST}")
print(f"         Server   : {ENV.TWINLAB_SERVER}")
print()
