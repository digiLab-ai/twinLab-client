# Standard imports
from typing import Optional

# Third-party imports
from pydantic import BaseSettings


class Environment(BaseSettings):
    TWINLAB_TRAINING_SERVER: Optional[str]
    TWINLAB_SERVER: str
    TWINLAB_GROUPNAME: str
    TWINLAB_USERNAME: str
    TWINLAB_TOKEN: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()

# if not ENV.TWINLAB_TRAINING_SERVER:
#     print(
#         f"""
#         === TwinLab Client Initialisation ===
#         Server   : {ENV.TWINLAB_SERVER}
#         Group    : {ENV.TWINLAB_GROUPNAME}
#         User     : {ENV.TWINLAB_USERNAME}
#         """
#     )
# else:
#     print(
#         f"""
#         === TwinLab Client Initialisation ===
#         Training : {ENV.TWINLAB_TRAINING_SERVER}
#         Server   : {ENV.TWINLAB_SERVER}
#         Group    : {ENV.TWINLAB_GROUPNAME}
#         User     : {ENV.TWINLAB_USERNAME}
#         """
#     )
print()
print("         === TwinLab Client Initialisation ===")
if ENV.TWINLAB_TRAINING_SERVER:
    print(f"         Training : {ENV.TWINLAB_TRAINING_SERVER}")
print(f"         Server   : {ENV.TWINLAB_SERVER}")
print(f"         Group    : {ENV.TWINLAB_GROUPNAME}")
print(f"         User     : {ENV.TWINLAB_USERNAME}")
print()
