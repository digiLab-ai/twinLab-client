# Standard imports
import io
import json
from typing import Union, Tuple
from pprint import pprint
import time

# Third-party imports
import pandas as pd
from typeguard import typechecked

# Project imports
from . import api
from . import utils
from .settings import ENV

# Parameters
WAIT_TIME = 1.  # For polling model [s]

### Utility functions ###


@typechecked
def _status_campaign(campaign_id: str, verbose=False, debug=False) -> dict:
    response = api.status_model(campaign_id, verbose=debug)
    if verbose:
        message = _get_message(response)
        print(message, "\n")
    return response


@typechecked
def _use_campaign(filepath_or_df: Union[str, pd.DataFrame], campaign_id: str, method: str,
                  verbose=False, debug=False, check=False) -> pd.DataFrame:

    if type(filepath_or_df) is str:
        filepath = filepath_or_df
        eval_csv = open(filepath, "rb").read()
    else:
        df = filepath_or_df
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        eval_csv = buffer.getvalue()
    if check:
        utils.check_dataset(eval_csv.decode("utf-8"))
    output_csv = api.use_model(eval_csv, campaign_id, method=method,
                               processor="cpu", verbose=debug)
    df = pd.read_csv(io.StringIO(output_csv), sep=",")
    return df


def _get_message(response: dict) -> str:
    try:
        message = response["message"]
    except:
        message = response
    return message

### ###

### General functions ###


@typechecked
def get_user_information(verbose=False, debug=False) -> dict:
    """
    # Get user information

    Get information about the user

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    - `dict` containing user information

    ## Example
    ```
    import twinlab as tl

    user_info = tl.get_user_information()
    print(user_info)
    ```
    """
    user_info = api.get_user(verbose=debug)
    if verbose:
        print("User information:")
        pprint(user_info, compact=True, sort_dicts=False)
        print()
    return user_info


@typechecked
def get_versions(verbose=False, debug=False) -> dict:
    """
    # Get versions

    Get information about the twinLab version being used

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    - `dict` containing version information

    ## Example
    ```
    import twinlab as tl

    version_info = tl.get_versions()
    print(version_info)
    ```
    """
    version_info = api.get_versions(verbose=debug)
    if verbose:
        print("Version information:")
        pprint(version_info, compact=True, sort_dicts=False)
        print()
    return version_info

### ###

### Dataset functions ###


@typechecked
def upload_dataset(filepath_or_df: Union[str, pd.DataFrame], dataset_id: str,
                   verbose=False, debug=False, use_url=True, check_dataset=True) -> None:
    """
    # Upload dataset

    Upload a dataset to the `twinLab` cloud so that it can be queried and used for training.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str` | `Dataframe`; location of csv dataset on local machine or `pandas` dataframe
    - `dataset_id`: `str`; name for the dataset when saved to the twinLab cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server
    - `use_url`: `bool` upload via a pre-signed url or directly to the server
    - `check`: `bool` check the dataset is sensible before uploading

    **NOTE:** Local data must be a CSV file, working data should be a pandas Dataframe. 
    In either case a `dataset_id` must be provided.

    ## Examples

    Upload a local file:
    ```python
    import twinlab as tl

    data_filepath = "resources/data/my_data.csv"
    tl.upload_dataset(data_filepath, "my_dataset") # This will be my_data.csv in the cloud
    ```

    Upload a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    dataframe = pd.DataFrame({'X': [1, 2, 3, 4], 'y': [1, 4, 9, 16]})
    tl.upload_dataset(dataframe, "my_dataset")
    ```
    """

    # Upload the file (either via link or directly)
    if use_url:
        upload_url = api.generate_upload_url(dataset_id, verbose=debug)
        if type(filepath_or_df) is str:
            filepath = filepath_or_df
            utils.upload_file_to_presigned_url(
                filepath, upload_url, verbose=verbose, check=check_dataset)
        elif type(filepath_or_df) is pd.DataFrame:
            df = filepath_or_df
            utils.upload_dataframe_to_presigned_url(
                df, upload_url, verbose=verbose, check=check_dataset)
        else:
            raise ValueError(
                "filepath_or_df must be a string or pandas dataframe")
        response = api.process_uploaded_dataset(dataset_id, verbose=debug)

    else:
        if type(filepath_or_df) is str:
            filepath = filepath_or_df
            csv_string = open(filepath, "rb").read()
        elif type(filepath_or_df) is pd.DataFrame:
            df = filepath_or_df
            buffer = io.BytesIO()
            df.to_csv(buffer, index=False)
            csv_string = buffer.getvalue()
        else:
            raise ValueError(
                "filepath_or_df must be a string or pandas dataframe")
        if check_dataset:
            utils.check_dataset(csv_string.decode("utf-8"))
        response = api.upload_dataset(csv_string, dataset_id, verbose=debug)

    if verbose:
        message = _get_message(response)
        print(message)


@typechecked
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


@typechecked
def view_dataset(dataset_id: str, verbose=False, debug=False) -> pd.DataFrame:
    """
    # View dataset

    View a dataset that exists on the twinLab cloud.

    ## Arguments

    - `dataset_id`: `str`; name for the dataset when saved to the twinLab cloud
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    - `pandas.DataFrame` of the dataset.


   ## Example

    ```python
    import twinlab as tl

    df = tl.view_dataset("my_dataset")
    print(df)
    ```
    """
    response = api.view_dataset(dataset_id, verbose=debug)
    csv_string = io.StringIO(response)
    df = pd.read_csv(csv_string, sep=",")
    if verbose:
        print("Dataset:")
        print(df)
        print()
    return df


@typechecked
def query_dataset(dataset_id: str, verbose=False, debug=False) -> pd.DataFrame:
    """
    # Query dataset

    Query a dataset that exists on the `twinLab` cloud by printing summary statistics.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `dataset_id`: `str`; name of dataset on S3 (same as the uploaded file name)
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    - `pandas.DataFrame` containing summary statistics for the dataset.

    ## Example

    ```python
    import twinlab as tl

    df = tl.query_dataset("my_dataset")
    print(df)
    ```
    """
    response = api.summarise_dataset(dataset_id, verbose=debug)
    csv_string = io.StringIO(response)
    df = pd.read_csv(csv_string, sep=",")
    if verbose:
        print("Dataset summary:")
        print(df)
        print()
    return df


@typechecked
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

    - `list` of `str` dataset ids

    ## Example

    ```python
    import twinlab as tl

    tl.delete_dataset("my_dataset")
    ```
    """
    response = api.delete_dataset(dataset_id, verbose=debug)
    if verbose:
        message = _get_message(response)
        print(message, "\n")

###  ###

### Campaign functions ###


@typechecked
def train_campaign(filepath_or_params: Union[str, dict], campaign_id: str,
                   verbose=False, debug=False) -> None:
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
    import twinlab as tl

    tl.train_campaign("path/to/params.json", "my_campaign")
    ```

    Train via a `python` dictionary:
    ```python
    import twinlab as tl

    params = {
        "dataset_id": "my_dataset",
        "inputs": ["X"],
        "outputs": ["y"],
    }
    tl.train_campaign(params, "my_campaign")
    ```
    """
    if type(filepath_or_params) is dict:
        params = filepath_or_params
    elif type(filepath_or_params) is str:
        filepath = filepath_or_params
        params = json.load(open(filepath))
    else:
        print("Type:", type(filepath_or_params))
        raise ValueError(
            "filepath_or_params must be either a string or a dictionary")
    params = utils.coerce_params_dict(params)
    params_str = json.dumps(params)
    response = api.train_model(
        params_str, campaign_id, processor="cpu", verbose=debug)
    if verbose:
        message = _get_message(response)
        print(message, "\n")

    # Wait for job to complete
    complete = False
    while not complete:
        status = _status_campaign(campaign_id, verbose=False, debug=debug)
        complete = status["job_complete"]
        time.sleep(WAIT_TIME)


@typechecked
def list_campaigns(verbose=False, debug=False) -> list:
    """
    # List datasets

    List campaigns that have been completed to the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    ## Returns

    - A `list` of `str` campaign ids

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


@typechecked
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

    - dictionary containing summary statistics for the dataset.

    ## Example

    ```python
    import twinlab as tl

    info = tl.query_campaign("my_campaign")
    print(info)
    ```
    """
    # TODO: This should eventually return a dataframe
    query = api.summarise_model(campaign_id, verbose=debug)
    if verbose:
        print("Model summary:")
        pprint(query, compact=True, sort_dicts=False)
        print()
    return query


@typechecked
def predict_campaign(filepath_or_df: Union[str, pd.DataFrame], campaign_id: str,
                     verbose=False, debug=False, check_dataset=True) -> Tuple[pd.DataFrame, pd.DataFrame]:
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

    - `tuple` containing:
        - `df_mean`: `pandas.DataFrame` containing mean predictions
        - `df_std`: `pandas.DataFrame` containing standard deviation predictions


    ## Example

    Using a local file:
    ```python
    import twinlab as tl

    filepath = "resources/data/eval.csv" # Local
    campaign_id = "my_campaign" # Pre-trained
    df_mean, df_std = tl.predict_campaign(file, campaign_id)
    ```

    Using a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    df = pd.DataFrame({'X': [1.5, 2.5, 3.5]})
    tl.predict_campaign(df, "my_campaign")
    ```
    """

    df = _use_campaign(filepath_or_df, campaign_id, method="predict",
                       verbose=verbose, debug=debug, check=check_dataset)

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


@typechecked
def sample_campaign(filepath_or_df: Union[str, pd.DataFrame], campaign_id: str,
                    verbose=False, debug=False, check_dataset=True) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    # Sample campaign

    Draw samples from a pre-trained campaign that exists on the `twinLab` cloud.

    **NOTE:** Your user information is automatically added to the request using the `.env` file.

    ## Arguments

    - `filepath_or_df`: `str`; location of csv dataset on local machine for evaluation or `pandas` dataframe
    - `campaign_id`: `str`; name of pre-trained campaign to use for predictions
    - `verbose`: `bool` determining level of information returned to the user
    - `debug`: `bool` determining level of information logged on the server

    **NOTE:** Evaluation data must be a CSV file, or a `pandas` dataframe that is interpretable as a CSV.

    ## Returns

    - `tuple` containing:
        - `df_mean`: `pandas.DataFrame` containing mean predictions
        - `df_std`: `pandas.DataFrame` containing standard deviation predictions


    ## Example

    Using a local file:
    ```python
    import twinlab as tl

    filepath = "resources/data/eval.csv" # Local
    campaign_id = "my_campaign" # Pre-trained
    df_mean, df_std = tl.sample_campaign(file, campaign_id)
    ```

    Using a `pandas` dataframe:
    ```python
    import pandas as pd
    import twinlab as tl

    df = pd.DataFrame({'X': [1.5, 2.5, 3.5]})
    tl.sample_campaign(df, "my_campaign")
    ```
    """

    df_samples = _use_campaign(filepath_or_df, campaign_id, method="sample",
                               verbose=verbose, debug=debug, check=check_dataset)
    # TODO: Munge to get the format correct
    return df_samples


@typechecked
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

    tl.delete_campaign("my_campaign")
    ```
    """
    response = api.delete_model(campaign_id, verbose=debug)
    if verbose:
        message = _get_message(response)
        print(message, "\n")

### ###
