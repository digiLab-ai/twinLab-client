# Standard imports
import requests
import json

# Project imports
from . import utils


def upload_data(training_file: str, user_info: dict, server="cloud", verbose=False) -> None:

    # Request URL
    baseURL = utils.get_server_url(server)
    url = baseURL+"/upload_data"

    # Request files to be sent to the lambda, including file type
    files = {"file": (training_file, open(training_file, "rb"), "text/csv")}

    # Request headers
    headers = utils.construct_headers(user_info)

    # Send request and print response
    r = requests.post(url, files=files, headers=headers)
    if verbose:
        utils.print_response(r)


def new_campaign(params_file: str, user_info: dict, server="cloud", verbose=False) -> None:

    # Request URL
    baseURL = utils.get_server_url(server)
    url = baseURL+"/new_campaign"

    # Request JSON file to be sent to the lambda
    with open(params_file) as f:
        params = json.load(f)

    # Request headers
    headers = utils.construct_headers(user_info)

    # Send request
    r = requests.post(url, json=params, headers=headers)
    if verbose:
        utils.print_response(r)


def sample_emulator(test_file: str, user_info: dict, server="cloud", verbose=False) -> tuple:

    # Request URL
    baseURL = utils.get_server_url(server)
    url = baseURL+"/sample_emulator"

    # Request files to be sent to the lambda, including file type
    files = {"file": (test_file, open(test_file, "rb"), "text/csv")}

    # Request headers
    headers = utils.construct_headers(user_info)

    # Send request and print response
    r = requests.post(url, files=files, headers=headers)
    if verbose:
        utils.print_response(r)

    # Extract dataframes from response
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
        print("Mean:", df_mean, "\n")
        print("Std:", df_std, "\n")
    return df_mean, df_std


def delete_campaign(user_info: dict, server="cloud", verbose=False) -> None:
    """
    Delete campaign directory from S3
    """

    # Request URL
    baseURL = utils.get_server_url(server)
    url = baseURL+"/delete_campaign"

    # Request headers
    headers = utils.construct_headers(user_info)

    # Send request and print response
    r = requests.post(url, headers=headers)
    if verbose:
        utils.print_response(r)

### ###
