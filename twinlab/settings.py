# Third-party imports
from pydantic import BaseSettings

# Project imports
from ._version import __version__
from . import api

# Parameters
# TODO: Move these into a settings.json?
WAIT_TIME = 1.                 # Poll time after job submission [s]
CHECK_DATASETS = True          # Check datasets are sensible before uploading
USE_UPLOAD_URL = True          # Upload via a pre-signed url or directly to the server
DEFAULT_TRAIN_TEST_RATIO = 1.  # Default fraction of data to use for training
PARAMS_COERCION = {            # Convert parameter names in params dict
    "test_train_ratio": "train_test_ratio",   # Common mistake
    "filename": "dataset_id",                 # Support old name
    "filename_std": "dataset_std_id",         # Support old name
    "dataset": "dataset_id",                  # Support old name
    "dataset_std": "dataset_std_id",          # Support old name
    "functional_input": "decompose_inputs",
    "functional_output": "decompose_outputs",
    "function_input": "decompose_inputs",
    "function_output": "decompose_outputs",
}


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
