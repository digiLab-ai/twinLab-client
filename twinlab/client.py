# Standard imports
import io
import json
from typing import Union, Tuple
from pprint import pprint

# Third-party imports
import pandas as pd

# Project imports
from . import api
from . import utils
from .settings import ENV

### Dataset functions ###


def get_user(verbose=False, debug=False) -> dict:
    """
    Get the user information
    """
    user_info = api.get_user(verbose=debug)
    if verbose:
        print("User information:")
        pprint(user_info, compact=True, sort_dicts=False)
        print()
    return user_info


def get_versions(verbose=False, debug=False) -> dict:
    """
    Get the version information about the twinLab version
    """
    version_info = api.get_versions(verbose=debug)
    if verbose:
        print("Version information:")
        pprint(version_info, compact=True, sort_dicts=False)
        print()
    return version_info


def upload_dataset(filepath_or_df: Union[str, pd.DataFrame], dataset_id: str, verbose=False, debug=False) -> None:
    """
    # Upload dataset

    Upload a dataset to the `twinLab` cloud so that it can be queried and used for training.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str` | `Dataframe`; location of csv dataset on local machine or `pandas` dataframe
    - `dataset_id`: `str`; name for the dataset when saved to the twinLab cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    **NOTE:** Local data must be a CSV file, working data should be a pandas Dataframe. 
    In either case a `dataset_id` must be provided.

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
    dataset_id = "test.csv" # Give the dataset a name in the cloud
    tl.upload_dataset(dataframe, dataset_id)
    ```
    """

    # Sort out dataset_id
    # if dataset_id is None:
    #     if type(filepath_or_df) == str:
    #         dataset_id = filepath_or_df
    #     else:
    #         raise ValueError(
    #             "A dataset_id must be specified if uploading a dataframe")
    # else:
    #     if ("/" in dataset_id) or ("\\" in dataset_id):
    #         raise ValueError("Dataset name cannot contain '/' or '\\'")

    # # Get the upload URL
    # headers = utils.construct_standard_headers(debug=debug)
    # headers["X-Dataset"] = dataset_id
    # lambda_url = ENV.TWINLAB_SERVER + "/generate_upload_url"
    # r = requests.get(lambda_url, headers=headers)
    # utils.check_response(r)

    # # Upload the file
    # if verbose:
    #     utils.print_response_message(r)
    # upload_url = r.json()["url"]
    # if type(filepath_or_df) is str:
    #     filepath = filepath_or_df
    #     utils.upload_file_to_presigned_url(
    #         filepath, upload_url, verbose=verbose)
    # else:
    #     df = filepath_or_df
    #     utils.upload_dataframe_to_presigned_url(
    #         df, upload_url, verbose=verbose)
    # if verbose:
    #     print(f"Uploading {dataset_id}")

    # # Process the uploaded dataset remotely
    # process_url = ENV.TWINLAB_SERVER + "/process_uploaded_dataset"
    # r = requests.post(process_url, headers=headers)
    # if verbose:
    #     utils.print_response_message(r)

    # TODO: Change to work with an upload URL
    # TODO: Check that this works with dataframes
    if type(filepath_or_df) is str:
        filepath = filepath_or_df
    elif type(filepath_or_df) is pd.DataFrame:
        df = filepath_or_df
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        filepath = buffer.getvalue()
    else:
        raise ValueError(
            "filepath_or_df must be a string or pandas dataframe")
    csv_string = open(filepath, "rb").read()
    response = api.upload_dataset(csv_string, dataset_id, verbose=debug)
    if verbose:
        print(response["message"])


def view_dataset(dataset_id: str, verbose=False, debug=False) -> pd.DataFrame:
    """
    # View dataset

    View a dataset that exists on the twinLab cloud.
    """
    response = api.view_dataset(dataset_id, verbose=debug)
    csv_string = io.StringIO(response)
    df = pd.read_csv(csv_string, sep=",")
    if verbose:
        print("Dataset:")
        print(df)
        print()
    return df


def query_dataset(dataset_id: str, verbose=False, debug=False) -> dict:
    """
    # Query dataset

    Query a dataset that exists on the `twinLab` cloud by printing summary statistics.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `dataset_id`: `str`; name of dataset on S3 (same as the uploaded file name)
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    `pandas` dataframe containing summary statistics for the dataset.

    ## Example

    ```python
    import twinlab as tl

    dataset_id = "my_dataset.csv"
    df = tl.query_dataset(dataset_id)
    print(df)
    ```
    """
    # TODO: This should eventally return a dataframe, but cloud needs to be modified for this
    query = api.summarise_dataset(dataset_id, verbose=debug)
    if verbose:
        print("Dataset summary:")
        pprint(query, compact=True, sort_dicts=False)
        print()
    return query


def list_datasets(verbose=False, debug=False) -> list:
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
    datasets = api.list_datasets(verbose=debug)
    if verbose:
        print("Datasets:")
        pprint(datasets, compact=True, sort_dicts=False)
        print()
    return datasets


def delete_dataset(dataset_id: str, verbose=False, debug=False) -> None:
    """
    # Delete dataset

    Delete a dataset from the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `dataset_id`: `str`; name of dataset to delete from the cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    List of `str` dataset ids

    ## Example

    ```python
    import twinlab as tl

    dataset_id = "my_dataset.csv"
    tl.delete_dataset(dataset_id)
    ```
    """
    response = api.delete_dataset(dataset_id, verbose=debug)
    if verbose:
        print(response["message"])
        print()

###  ###

### Campaign functions ###


def train_campaign(filepath_or_params: Union[str, dict], campaign_id: str, verbose=False, debug=False) -> None:
    """
    # Train campaign

    Train a campaign in the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_params`: `str` | `dict`; filepath to local json or parameters dictionary for training
    - `campaign_id`: `str`; name for the final trained campaign
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
    if type(filepath_or_params) is dict:
        params = filepath_or_params
    elif type(filepath_or_params) is str:
        filepath = filepath_or_params
        params = json.load(open(filepath))
    else:
        print(type(filepath_or_params))
        raise ValueError(
            "filepath_or_params must be either a string or a dictionary")
    params = utils.coerce_params_dict(params)
    params_str = json.dumps(params)
    response = api.train_model(
        params_str, campaign_id, processor="cpu", verbose=debug)
    if verbose:
        print(response["message"])
        print()


def status_campaign(campaign_id: str, verbose=False, debug=False) -> dict:
    """
    """
    response = api.status_model(campaign_id, verbose=debug)
    if verbose:
        print(response["message"])
        print()
    return response


def query_campaign(campaign_id: str, verbose=False, debug=False) -> dict:
    """
    # Query campaign

    Get summary statistics for a pre-trained campaign in the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `campaign_id`: `str`; name of trained campaign to query
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
    # url = ENV.TWINLAB_SERVER + "/query_campaign"
    # headers = utils.construct_standard_headers(debug=debug)
    # headers["X-Campaign"] = campaign_id
    # r = requests.get(url, headers=headers)
    # utils.check_response(r)
    # metadata = utils.extract_item_from_response(r, "metadata")
    # if verbose:
    #     utils.print_response_message(r)
    #     print("Metadata:")
    #     pprint(metadata, compact=True, sort_dicts=False)
    # return metadata
    # TODO: This should eventally return a dataframe, but cloud needs to be modified for this
    query = api.summarise_model(campaign_id, verbose=debug)
    if verbose:
        print("Model summary:")
        pprint(query, compact=True, sort_dicts=False)
        print()
    return query


def list_campaigns(verbose=False, debug=False) -> list:
    """
    # List datasets

    List campaigns that have been completed to the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    A list of `str` campaign ids

    ## Example

    ```python
    import twinlab as tl

    campaigns = tl.list_campaigns()
    print(campaigns)
    ```
    """
    campaigns = api.list_models(verbose=debug)
    if verbose:
        print("Trained models:")
        pprint(campaigns, compact=True, sort_dicts=False)
        print()
    return campaigns


def predict_campaign(
    filepath_or_df: Union[str, pd.DataFrame], campaign_id: str, verbose=False, debug=False
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    # Predict campaign

    Predict from a pre-trained campaign that exists on the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str`; location of csv dataset on local machine for evaluation or `pandas` dataframe
    - `campaign_id`: `str`; name of pre-trained campaign to use for predictions
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
    campaign_id = "my_campaign" # Pre-trained
    df_mean, df_std = tl.sample_campaign(file, campaign_id)
    ```

    Use a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    df= pd.DataFrame({'X': [1.5, 2.5, 3.5]}
    campaign_id = "my_campaign" # Pre-trained
    tl.predict_campaign(df, campaign_id)
    ```
    """
    if type(filepath_or_df) is str:
        filepath = filepath_or_df
    else:
        df = filepath_or_df
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        filepath = buffer.getvalue()
    eval_csv = open(filepath, "rb").read()
    output_csv = api.use_model(
        eval_csv, campaign_id, method="predict", processor="cpu", verbose=debug)
    df = pd.read_csv(io.StringIO(output_csv), sep=",")
    n = len(df.columns)
    df_mean, df_std = df.iloc[:, :n//2], df.iloc[:, n//2:]
    df_std.columns = df_std.columns.str.removesuffix(" [std_dev]")
    if verbose:
        print("Mean predictions:")
        print(df_mean)
        print()
        print("Standard deviation predictions:")
        print(df_std)
        print()
    return df_mean, df_std


def delete_campaign(campaign_id: str, verbose=False, debug=False) -> None:
    """
    # Delete campaign

    Delete campaign from the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `campaign_id`: `str`; name of trained campaign to delete from the cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Example

    ```python
    import twinlab as tl

    campaign = "my_campaign"
    tl.delete_campaign(campaign)
    ```
    """
    response = api.delete_model(campaign_id, verbose=debug)
    if verbose:
        print(response["message"])
        print()
