# Standard imports
from pprint import pprint

# Third-party imports
import requests
import pandas as pd

# Project imports
from . import utils


def upload_dataset(training_file: str, server="cloud", verbose=False) -> None:
    """
    Upload dataset
    """
    url = utils.get_server_url(server) + "/upload_dataset"
    files = {"file": (training_file, open(training_file, "rb"), "text/csv")}
    headers = utils.STANDARD_HEADERS.copy()  #  TODO: Is .copy() necessary?
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def query_dataset(dataset: str, server="cloud", verbose=False) -> pd.DataFrame:
    """
    Query dataset
    """
    url = utils.get_server_url(server) + "/query_dataset"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Dataset"] = dataset
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    df = utils.extract_csv_from_response(r, "summary")
    if verbose:
        utils.print_response_message(r)
        print("Summary:\n", df, "\n")
    return df


def list_datasets(server="cloud", verbose=False) -> list:
    """
    List datasets in S3
    """
    url = utils.get_server_url(server) + "/list_datasets"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def delete_dataset(dataset: str, server="cloud", verbose=False) -> None:
    """
    Delete campaign directory from S3
    """
    url = utils.get_server_url(server) + "/delete_dataset"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Dataset"] = dataset
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def train_campaign(params: dict, campaign: str, server="cloud", verbose=False) -> None:
    """
    Train campaign
    TODO: Set default train_test_split?
    """
    url = utils.get_server_url(server) + "/train_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, json=params, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def query_campaign(campaign: str, server="cloud", verbose=False) -> pd.DataFrame:
    """
    Query campaign
    """
    url = utils.get_server_url(server) + "/query_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    metadata = utils.extract_item_from_response(r, "metadata")
    if verbose:
        utils.print_response_message(r)
        print("Metadata:")
        pprint(metadata)
    return metadata


def list_campaigns(server="cloud", verbose=False) -> list:
    """
    List campaigns in S3
    """
    url = utils.get_server_url(server) + "/list_campaigns"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def sample_campaign(
    test_file: str, campaign: str, server="cloud", verbose=False
) -> tuple:
    """
    Sample campaign
    """
    url = utils.get_server_url(server) + "/sample_campaign"
    files = {"file": (test_file, open(test_file, "rb"), "text/csv")}
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
        utils.print_response_message(r)
        print("Mean:", df_mean, "\n")
        print("Std:", df_std, "\n")
    return df_mean, df_std


def delete_campaign(campaign: str, server="cloud", verbose=False) -> None:
    """
    Delete campaign directory from S3
    """
    url = utils.get_server_url(server) + "/delete_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)


def delete_dataset(dataset: str, server="cloud", verbose=False) -> None:
    """
    Delete campaign directory from S3
    """
    url = utils.get_server_url(server) + "/delete_dataset"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Dataset"] = dataset
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)


def list_campaigns(server="cloud", verbose=False) -> list:
    """
    List campaigns in S3
    """
    url = utils.get_server_url(server) + "/list_campaigns"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)

    response = r.json()
    return response["campaign_ids"]


def list_datasets(server="cloud", verbose=False) -> list:
    """
    List datasets in S3
    """
    url = utils.get_server_url(server) + "/list_datasets"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)
    response = r.json()
    return response["datasets"]
