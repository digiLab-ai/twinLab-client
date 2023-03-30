# Standard imports
import argparse

# Third-party imports
import requests
import pandas as pd

# Project imports
from .settings import ENV


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


def extract_csv_from_response(response: requests.Response, name: str) -> pd.DataFrame:
    """
    Extract CSV from response
    """
    body = response.json()  # Get the body of the response as a dictionary
    data = body[name]  # Get the entry corresponding to the field name
    df = pd.read_json(data, orient="split")
    return df


def construct_headers(user_info: dict) -> dict:
    """
    Construct headers for request
    """

    user_info = user_info.update(
        {
            "group": ENV.GROUP_NAME,
            "user": ENV.USER_NAME,
        }
    )

    headers = {
        "X-Group": user_info["group"],
        "X-User": user_info["user"],
        "X-Campaign": user_info["campaign"],
    }
    return headers


def print_response(r: requests.Response) -> None:
    """
    Print response
    """
    print("Response headers:", r.headers, "\n")
    print("Response text:", r.text, "\n")
