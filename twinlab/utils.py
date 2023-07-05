# Standard imports
import io

# Third-party imports
import requests
import numpy as np
import pandas as pd

# Project imports
from . import settings

### Utility functions ###


def coerce_params_dict(params: dict) -> dict:
    """
    Relabel parameters to be consistent with twinLab library
    """
    if "train_test_split" in params.keys() or "test_train_split" in params.keys():
        raise TypeError(
            "train_test_split is deprecated. Use train_test_ratio instead.")
    for param in settings.PARAMS_COERCION:
        if param in params:
            params[settings.PARAMS_COERCION[param]] = params.pop(param)
    if "train_test_ratio" not in params.keys():
        params["train_test_ratio"] = settings.DEFAULT_TRAIN_TEST_RATIO
    return params


def check_dataset(string: str) -> None:
    """
    Check that a sensible dataframe can be created from a CSV string.
    """

    # Can we parse the string into a dataframe?
    try:
        string_io = io.StringIO(string)
        df = pd.read_csv(string_io)
    except Exception:
        raise TypeError("Could not parse the input into a dataframe.")

    # Check that dataset has at least one column.
    if df.shape[0] < 1:
        raise TypeError("Dataset must have at least one column.")

    # Check that dataset has no duplicate column names.
    # TODO: Is this needed? What if the columns with identical names are not used in training?
    if len(set(df.columns)) != len(df.columns):
        raise TypeError("Dataset must contain no duplicate column names.")

    # Check that dataset has at least one row.
    if df.shape[1] < 1:
        raise TypeError("Dataset must have at least one row.")

    # Check that the dataset contains only numerical values.
    if not df.applymap(lambda x: isinstance(x, (int, float))).all().all():
        raise Warning("Dataset contains non-numerical values.")

    # Warning if the dataset contains missing values.
    if df.isnull().values.any():
        raise Warning("Dataset contains missing values.")

    # Warning if the dataset contains infinite values.
    if not np.isfinite(df).all().all():
        raise Warning("Dataset contains infinite values.")

### ###

### HTTP requests ###


def upload_file_to_presigned_url(file_path: str, url: str, verbose=False, check=False) -> None:
    """
    Upload a file to the specified pre-signed URL.
    params:
        file_path: str; the path to the local file you want to upload.
        presigned_url: The pre-signed URL generated for uploading the file.
        verbose: bool
    """
    if check:
        with open(file_path, "rb") as file:
            csv_string = file.read().decode("utf-8")
            check_dataset(csv_string)
    with open(file_path, "rb") as file:
        headers = {"Content-Type": "application/octet-stream"}
        response = requests.put(url, data=file, headers=headers)
    if verbose:
        if response.status_code == 200:
            print(f"File {file_path} is uploading.")
        else:
            print(f"File upload failed")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.text}")


def upload_dataframe_to_presigned_url(df: pd.DataFrame, url: str, verbose=False, check=False) -> None:
    """
    Upload a panads dataframe to the specified pre-signed URL.
    params:
        df: The pandas dataframe to upload
        url: The pre-signed URL generated for uploading the file.
        verbose: bool
    """
    if check:
        csv_string = df.to_csv(index=False)
        check_dataset(csv_string)
    headers = {"Content-Type": "application/octet-stream"}
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    buffer = buffer.getvalue()
    response = requests.put(url, data=buffer, headers=headers)
    if verbose:
        if response.status_code == 200:
            print(f"Dataframe is uploading.")
        else:
            print(f"File upload failed")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.text}")

### ###
