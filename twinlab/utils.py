# Standard imports
import io

# Third-party imports
import requests
import pandas as pd

# Convert these names in the params file
PARAMS_COERCION = {
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


### Utility functions ###


def coerce_params_dict(params: dict) -> dict:
    """
    Relabel parameters to be consistent with twinLab library
    """
    for param in PARAMS_COERCION:
        if param in params:
            params[PARAMS_COERCION[param]] = params.pop(param)
    return params


### ###

### HTTP requests ###


def upload_file_to_presigned_url(file_path: str, url: str, verbose=False) -> None:
    """
    Upload a file to the specified pre-signed URL.
    params:
        file_path: str; the path to the local file you want to upload.
        presigned_url: The pre-signed URL generated for uploading the file.
        verbose: bool
    """

    with open(file_path, "rb") as file:
        headers = {"Content-Type": "application/octet-stream"}
        response = requests.put(url, data=file, headers=headers)
    if verbose:
        if response.status_code == 200:
            print(f"File {file_path} uploaded successfully.")
        else:
            print(f"File upload failed")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.text}")
        print()


def upload_dataframe_to_presigned_url(df: pd.DataFrame, url: str, verbose=False) -> None:
    """
    Upload a panads dataframe to the specified pre-signed URL.
    params:
        df: The pandas dataframe to upload
        url: The pre-signed URL generated for uploading the file.
        verbose: bool
    """
    headers = {"Content-Type": "application/octet-stream"}
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    buffer = buffer.getvalue()
    response = requests.put(url, data=buffer, headers=headers)
    if verbose:
        if response.status_code == 200:
            print(f"Dataframe uploaded successfully.")
        else:
            print(f"File upload failed")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.text}")
        print()

### ###
