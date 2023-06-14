# Standard imports
from typing import Optional

# Third-party imports
from pydantic import BaseSettings


class Environment(BaseSettings):
    TWINLAB_SERVER: str
    RAPIDAPI_SUBSCRIPTION: str
    RAPIDAPI_USER: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()

print(
    f"""
    === TwinLab Client Initialisation ===
    Server       : {ENV.TWINLAB_SERVER}
    Subscription : {ENV.RAPIDAPI_SUBSCRIPTION}
    User         : {ENV.RAPIDAPI_USER}
    """
)
