# Third-party imports
import requests

# Project imports
from . import utils


def upload_dataset(
    training_file: str, server="cloud", verbose=False
) -> None:
    """
    Upload dataset
    """
    url = utils.get_server_url(server) + "/upload_dataset"
    files = {"file": (training_file, open(training_file, "rb"), "text/csv")}
    headers = utils.STANDARD_HEADERS.copy()  #  TODO: Is .copy() necessary?
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)


def train_campaign(
    params: dict, campaign: str, server="cloud", verbose=False
) -> None:
    """
    Train campaign
    """
    url = utils.get_server_url(server) + "/train_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, json=params, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_text(r)


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
    if verbose:
        utils.print_response_text(r)

    # Extract dataframes from response
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
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
