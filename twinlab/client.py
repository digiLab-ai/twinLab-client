# Standard imports
import io
import json
from pprint import pprint
from typing import Union

# Third-party imports
import requests
import pandas as pd

# Project imports
from . import utils
from .settings import ENV

### Dataset functions ###


def upload_dataset(filepath_or_df: Union[str, pd.DataFrame], dataset_name=None, verbose=False, debug=False) -> None:
    """
    # Upload dataset

    Upload a dataset to the `twinLab` cloud so that it can be queried and used for training.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str` | `Dataframe`; location of csv dataset on local machine or `pandas` dataframe
    - `dataset_name`: `str`; name for the dataset when saved to the twinLab cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    **NOTE:** Local data must be a CSV file. If a `pandas` dataframe is uploaded then a `dataset_name` must be provided. 
    If a local file is uploaded then the filename with the directories removed will be the uploaded file name, 
    unless a value of `dataset_name` is provided, which will be used preferentially.

    ## Examples

    Upload a local file:
    ```python
    import twinlab as tl

    data_filepath = "resources/data/my_data.csv"
    tl.upload_dataset(data_filepath) # This will be my_data.csv in the cloud
    ```

    Upload a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    dataframe = pd.DataFrame({'X': [1, 2, 3, 4], 'y': [1, 4, 9, 16]})
    dataset_name = "test.csv" # Give the dataset a name in the cloud
    tl.upload_dataset(dataframe, dataset_name)
    ```
    """

    # Sort out dataset_name
    if dataset_name is None:
        if type(filepath_or_df) == str:
            dataset_name = filepath_or_df
        else:
            raise ValueError(
                "A dataset_name must be specified if uploading a dataframe")
    else:
        if ("/" in dataset_name) or ("\\" in dataset_name):
            raise ValueError("Dataset name cannot contain '/' or '\\'")

    # Get the upload URL
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_name
    lambda_url = ENV.TWINLAB_SERVER + "/generate_upload_url"
    r = requests.get(lambda_url, headers=headers)
    utils.check_response(r)

    # Upload the file
    if verbose:
        utils.print_response_message(r)
    upload_url = r.json()["url"]
    if type(filepath_or_df) is str:
        filepath = filepath_or_df
        utils.upload_file_to_presigned_url(
            filepath, upload_url, verbose=verbose)
    else:
        df = filepath_or_df
        utils.upload_dataframe_to_presigned_url(
            df, upload_url, verbose=verbose)
    if verbose:
        print(f"Uploading {dataset_name}")

    # Process the uploaded dataset remotely
    process_url = ENV.TWINLAB_SERVER + "/process_uploaded_dataset"
    r = requests.post(process_url, headers=headers)
    if verbose:
        utils.print_response_message(r)


def query_dataset(dataset_name: str, verbose=False, debug=False) -> pd.DataFrame:
    """
    # Query dataset

    Query a dataset that exists on the `twinLab` cloud by printing summary statistics.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `dataset_name`: `str`; name of dataset on S3 (same as the uploaded file name)
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    `pandas` dataframe containing summary statistics for the dataset.

    ## Example

    ```python
    import twinlab as tl

    dataset_name = "my_dataset.csv"
    df = tl.query_dataset(dataset_name)
    print(df)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/query_dataset"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_name
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    df = utils.extract_csv_from_response(r, "summary")
    if verbose:
        utils.print_response_message(r)
        print("Summary:\n", df, "\n")
    return df


def list_datasets(verbose=False, debug=False) -> Union[list, None]:
    """
    # List datasets

    List datasets that have been uploaded to the `twinLab` cloud

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Example

    ```python
    import twinlab as tl

    datasets = tl.list_datasets()
    print(datasets)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/list_datasets"
    headers = utils.construct_standard_headers(debug=debug)
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    datasets = r.json()["datasets"]
    if verbose and datasets:
        print("Datasets:")
        pprint(datasets)
    return datasets


def delete_dataset(dataset_name: str, verbose=False, debug=False) -> None:
    """
    # Delete dataset

    Delete a dataset from the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `dataset_name`: `str`; name of dataset to delete from the cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Example

    ```python
    import twinlab as tl

    dataset_name = "my_dataset.csv"
    tl.delete_dataset(dataset_name)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/delete_dataset"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Dataset"] = dataset_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)

###  ###

### Campaign functions ###


def train_campaign(filepath_or_params: Union[str, dict], campaign_name: str, verbose=False, debug=False) -> None:
    """
    # Train campaign

    Train a campaign in the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_params`: `str` | `dict`; filepath to local json or parameters dictionary for training
    - `campaign_name`: `str`; name for the final trained model
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Example

    Train using a local `json` parameters file:
    ```python
    tl.train_campaign("params.json", "my_campaign", verbose=True)
    ```

    Train via a `python` dictionary:
    ```python
    params = {
        "dataset": "my_dataset",
        "inputs": ["X1", "X2"],
        "outputs": ["y1", "y2"],
    }
    tl.train_campaign(params, "my_campaign", verbose=True)
    ```
    """
    long_training_server = ENV.TWINLAB_TRAINING_SERVER
    training_server = ENV.TWINLAB_SERVER + "/train_campaign"
    url = long_training_server if long_training_server else training_server
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign_name
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


def query_campaign(campaign_name: str, verbose=False, debug=False) -> dict:
    """
    # Query campaign

    Get summary statistics for a pre-trained campaign in the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `campaign_name`: `str`; name of trained model to query
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    dictionary containing summary statistics for the dataset.

    ## Example

    ```python
    import twinlab_client as tl

    campaign = "my_campaign"
    tl.query_campaign(campaign)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/query_campaign"
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


def list_campaigns(verbose=False, debug=False) -> Union[list, None]:
    """
    # List datasets

    List datasets that have been uploaded to the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    A list of `str` dataset names, or `None` if there are no datasets

    ## Example

    ```python
    import twinlab as tl

    datasets = tl.list_datasets()
    print(datasets)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/list_campaigns"
    headers = utils.construct_standard_headers(debug=debug)
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    campaigns = r.json()["campaigns"]
    if verbose and campaigns:
        print("Campaigns:")
        pprint(campaigns)
    return campaigns


def predict_campaign(
    filepath_or_df: Union[str, pd.DataFrame], campaign_name: str, verbose=False, debug=False
) -> tuple:
    """
    # Predict campaign

    Predict from a pre-trained campaign that exists on the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str`; location of csv dataset on local machine for evaluation or `pandas` dataframe
    - `campaign_name`: `str`; name of pre-trained model to use for predictions
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    **NOTE:** Evaluation data must be a CSV file, or a `pandas` dataframe that is interpretable as a CSV.

    ## Returns

    `tuple` containing:
    - `df_mean`: `pandas` dataframe containing mean predictions
    - `df_std`: `pandas` dataframe containing standard deviation predictions


    ## Example

    Use a local file:
    ```python
    import twinlab_client as tl

    filepath = "resources/data/eval.csv" # Local
    campaign_name = "my_campaign" # Pre-trained
    df_mean, df_std = tl.sample_campaign(file, campaign_name)
    ```

    Use a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    df= pd.DataFrame({'X': [1.5, 2.5, 3.5]}
    campaign_name = "my_campaign" # Pre-trained
    tl.upload_dataset(df, campaign_name)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/predict_campaign"
    if isinstance(filepath_or_df, pd.DataFrame):  # Data frames
        buffer = io.BytesIO()
        filepath_or_df.to_csv(buffer, index=False)
        buffer = buffer.getvalue()
        files = {"file": ("tmp.csv", buffer, "text/csv")}
    else:  # File paths
        files = {"file": (filepath_or_df, open(
            filepath_or_df, "rb"), "text/csv")}
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign_name
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
        utils.print_response_message(r)
        print("Mean: \n", df_mean, "\n")
        print("Std: \n", df_std, "\n")
    return df_mean, df_std


def delete_campaign(campaign_name: str, verbose=False, debug=False) -> None:
    """
    # Delete campaign

    Delete campaign from the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `campaign_name`: `str`; name of trained model to delete from the cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Example

    ```python
    import twinlab as tl

    campaign = "my_campaign"
    tl.delete_campaign(campaign)
    ```
    """
    url = ENV.TWINLAB_SERVER + "/delete_campaign"
    headers = utils.construct_standard_headers(debug=debug)
    headers["X-Campaign"] = campaign_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
