from pydantic import BaseSettings


class Environment(BaseSettings):
    TWINLAB_LOCAL_SERVER: str
    TWINLAB_STAGE_SERVER: str
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

print(
    f"""
      == TwinLab Client Initialisation ==
      Server  : {ENV.TWINLAB_SERVER}
      Group   : {ENV.TWINLAB_GROUPNAME}
      User    : {ENV.TWINLAB_USERNAME}
      """
)
