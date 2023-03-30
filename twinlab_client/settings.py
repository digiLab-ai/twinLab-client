from pydantic import BaseSettings


class Environment(BaseSettings):
    LOCAL_SERVER: str
    CLOUD_SERVER: str
    GROUP_NAME: str
    USER_NAME: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()

print(
    f"""
      == Client Initialisation ==
      Local Server  : {ENV.LOCAL_SERVER}
      Cloud Server  : {ENV.CLOUD_SERVER}
      Group Name    : {ENV.GROUP_NAME}
      User Name     : {ENV.USER_NAME}
      """
)
