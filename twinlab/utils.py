# Standard imports
import argparse
import json
from pprint import pprint

# Third-party imports
import requests
import numpy as np
import pandas as pd

# Project imports
from .settings import ENV

STANDARD_HEADERS = {
    "X-Group": ENV.GROUP_NAME,
    "X-User": ENV.USER_NAME,
}

### Plotting ###


def get_blur_boundaries(n: int) -> np.ndarray:
    """
    Get boundaries for making a nice probability distribution of a Gaussian
    """
    frac = 1./(2.*(n+1.))
    fmin, fmax = frac, 1.-frac
    f = np.linspace(fmin, fmax, n)
    dy = -np.sqrt(2.)*np.log(f)
    return dy


def get_blur_alpha(n: int, alpha_mid=0.99) -> float:
    """
    Get a sensible alpha value for a given number of samples
    """
    alpha = 1.-(1.-alpha_mid)**(1/n)
    return alpha

###  ###

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
        default=False,
        help="specify whether to use local or cloud lambda function",
    )
    args = parser.parse_args()
    return args


def get_server_url(server: str) -> str:
    """
    The URL is the dockerised lambda function that's been set up in cloud by alexander
    """
    if server == "local":
        baseURL = ENV.LOCAL_SERVER
    elif server == "cloud":
        baseURL = ENV.CLOUD_SERVER
    else:
        print("Server:", server)
        raise ValueError("Server must be either 'local' or 'cloud'")
    return baseURL

### ###

### HTTP requests ###


def upload_file_to_presigned_url(file_path, presigned_url, verbose=False):
    """
    Upload a file to the specified pre-signed URL.

    :param file_path: The path to the file you want to upload.
    :param presigned_url: The pre-signed URL generated for uploading the file.
    :return: True if the upload is successful, False otherwise.
    """

    with open(file_path, "rb") as file:
        headers = {"Content-Type": "application/octet-stream"}
        response = requests.put(presigned_url, data=file, headers=headers)
    if verbose:
        if response.status_code == 200:
            print(f"File {file_path} uploaded successfully.")
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


def extract_item_from_response(response: requests.Response, name: str) -> pd.DataFrame:
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


# def print_response_text(r: requests.Response) -> None:
#     """
#     Print response message
#     """
#     print("Response:")
#     for key, value in json.loads(r.text).items():
#         print(f"{key}: {value}")
#     print()
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
        raise RuntimeError("Response error")\

### ###
