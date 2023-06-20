# Third-party imports
from pydantic import BaseSettings

# Project imports
from ._version import __version__


class Environment(BaseSettings):
    TWINLAB_SERVER: str
    TWINLAB_USERNAME: str
    RAPIDAPI_SUBSCRIPTION: str
    RAPIDAPI_USER: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()

print()
print("         === TwinLab Client Initialisation ===")
print(f"         Version  : {__version__}")
print(f"         Server   : {ENV.TWINLAB_SERVER}")
print(f"         User     : {ENV.TWINLAB_USERNAME}")
print()
