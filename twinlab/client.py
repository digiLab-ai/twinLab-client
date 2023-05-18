# Standard imports
import io
import json
from pprint import pprint

# Third-party imports
import requests
import pandas as pd

# Project imports
from . import utils

### Dataset functions ###


def upload_dataset(dataset_filepath: str, df=None, server="cloud", verbose=False, debug=False) -> None:
    """
    Upload a dataset to the cloud so that it can be queried and used for training
    params:
        dataset_filepath: str; location of csv dataset on local machine
        dt: None or pd.DataFrame; if None, then dataset_filepath is used to load the dataframe
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_filepath
    lambda_url = utils.get_server_url(server) + "/generate_upload_url"
    r = requests.get(lambda_url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    upload_url = r.json()["url"]
    if df is None:
        utils.upload_file_to_presigned_url(
            dataset_filepath, upload_url, verbose=verbose)
    else:
        dataset_name = dataset_filepath
        if "/" in dataset_name:
            raise ValueError("Dataset name cannot contain '/'")
        utils.upload_dataframe_to_presigned_url(dataset_name,
                                                df, upload_url, verbose=verbose)
    if verbose:
        print(f"Uploading {dataset_filepath}")
    process_url = utils.get_server_url(server) + "/process_uploaded_dataset"
    r = requests.post(process_url, headers=headers)
    if verbose:
        utils.print_response_message(r)


def query_dataset(dataset_name: str, server="cloud", verbose=False, debug=False) -> pd.DataFrame:
    """
    Query a dataset that exists on the cloud by printing summary statistics
    params:
        dataset_name: str; name of dataset on S3 (same as the uploaded file name)
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/query_dataset"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_name
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    df = utils.extract_csv_from_response(r, "summary")
    if verbose:
        utils.print_response_message(r)
        print("Summary:\n", df, "\n")
    return df


def list_datasets(server="cloud", verbose=False, debug=False) -> list:
    """
    List datasets that have been uploaded to the cloud
    params:
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/list_datasets"
    headers = utils.construct_standard_headers(debug=debug)
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    response = r.json()
    return response["datasets"]


def delete_dataset(dataset_name: str, server="cloud", verbose=False, debug=False) -> None:
    """
    Delete a dataset from the cloud
    params:
        dataset_name: str; name of dataset on S3 (same as the uploaded file name)
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/delete_dataset"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)

###  ###

### Campaign functions ###


def train_campaign(filepath_or_params, campaign: str, server="cloud", verbose=False, debug=False) -> None:
    """
    Train a campaign remotely using twinLab
    params:
        filepath_or_params: str or dict; filepath to json or parameters dict for training
        campaign: str; name of this campaign and final trained model (user choice)
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_train_campaign_url(server)
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign
    if isinstance(filepath_or_params, str):
        filepath = filepath_or_params
        with open(filepath) as f:
            params = json.load(f)
    else:
        params = filepath_or_params
    params = utils.coerce_params_dict(params)
    r = requests.post(url, json=params, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def query_campaign(campaign_name: str, server="cloud", verbose=False, debug=False) -> dict:
    """
    Print summary statistics for a pre-trained campaign
    params:
        campaign_name: str; name of trained model to query
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/query_campaign"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign_name
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    metadata = utils.extract_item_from_response(r, "metadata")
    if verbose:
        utils.print_response_message(r)
        print("Metadata:")
        pprint(metadata, compact=True, sort_dicts=False)
    return metadata


def list_campaigns(server="cloud", verbose=False, debug=False) -> list:
    """
    List all trained campaigns stored in cloud
    params:
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/list_campaigns"
    headers = utils.construct_standard_headers(debug=debug)
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    response = r.json()
    return response["campaigns"]


def predict_campaign(
    filepath_or_df, campaign: str, server="cloud", verbose=False, debug=False
) -> tuple:
    """
    Predict from a pre-trained campaign that exists on the cloud
    params:
        filepath: str; location of csv dataset on local machine for evaluation
        campaign: str; name of pre-trained model to do the evaluating
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(
        server) + "/predict_campaign"
    if isinstance(filepath_or_df, pd.DataFrame):  # Data frames
        buffer = io.BytesIO()
        filepath_or_df.to_csv(buffer, index=False)
        buffer = buffer.getvalue()
        files = {"file": ("tmp.csv", buffer, "text/csv")}
    else:  # File paths
        files = {"file": (filepath_or_df, open(
            filepath_or_df, "rb"), "text/csv")}
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
        utils.print_response_message(r)
        print("Mean: \n", df_mean, "\n")
        print("Std: \n", df_std, "\n")
    return df_mean, df_std


def delete_campaign(campaign_name: str, server="cloud", verbose=False, debug=False) -> None:
    """
    Delete campaign directory from S3
    params:
        campaign_name: str; name of trained model to delete
        server: str; either "cloud" or "local"
        verbose: bool
        debug: bool
    """
    url = utils.get_server_url(server) + "/delete_campaign"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
