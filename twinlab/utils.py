# Standard imports
import io
import argparse
import json
from pprint import pprint

# Third-party imports
import requests
import pandas as pd

# Project imports
from .settings import ENV

# Convert these names in the params file
PARAMS_COERCION = {
    "test_train_split": "train_test_split",  # Common mistake
    "num_training_examples": "train_test_split",  #  TODO: Think of something better
    "filename": "dataset",  # Suppoprt old name
    "filename_std": "dataset_std",  # Support old name
}


### Utility functions ###


# def unwrap_payload(event: dict) -> dict:
#     """
#     Return payload and decode if it is base64 encoded
#     TODO: Not used yet...
#     """
#     if "body" not in event:  # Get body
#         raise Exception("No body in request")
#     body = event["body"]
#     if "isBase64Encoded" in event:  # Decode
#         if event["isBase64Encoded"]:
#             body = base64.b64decode(body)
#     try:  # Parse
#         payload = json.loads(body)
#     except:
#         raise Exception("Could not parse body as JSON")
#     return payload


def get_command_line_args() -> argparse.Namespace:
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "server",
        default="cloud",
        nargs='?',
        help="Specify whether to use local or cloud lambda function",
    )
    args = parser.parse_args()
    return args


def construct_standard_headers(debug=False) -> dict:
    headers = {
        "X-Group": ENV.TWINLAB_GROUPNAME,
        "X-User": ENV.TWINLAB_USERNAME,
        "authorizationToken": ENV.TWINLAB_TOKEN,
        "X-Debug": str(debug).lower(),
    }
    return headers


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
        presigned_url: The pre-signed URL generated for uploading the file.
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


def extract_csv_from_response(response: requests.Response, name: str) -> pd.DataFrame:
    """
    Extract CSV from response
    """
    body = response.json()  # Get the body of the response as a dictionary
    data = body[name]  # Get the entry corresponding to the field name
    df = pd.read_json(data, orient="split")
    return df


def extract_item_from_response(response: requests.Response, name: str) -> any:
    """
    Extract CSV from response
    """
    body = response.json()  # Get the body of the response as a dictionary
    item = body[name]  # Get the entry corresponding to the field name
    return item


def print_response_headers(r: requests.Response) -> None:
    """
    Print response headers
    """
    print("Response headers:")
    pprint(dict(r.headers))
    print()


def print_response_message(r: requests.Response) -> None:
    """
    Print response message
    """
    print("Response:", json.loads(r.text)["message"])
    print()


def check_response(r: requests.Response) -> None:
    if r.status_code != 200:
        print("Status code:", r.status_code)
        print_response_message(r)
        raise RuntimeError("Response error")

### ###
