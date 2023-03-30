# Standard imports
import argparse
import json
from pprint import pprint

# Third-party imports
import requests
import pandas as pd

# Project imports
from .settings import ENV

STANDARD_HEADERS = {
    "X-Group": ENV.GROUP_NAME,
    "X-User": ENV.USER_NAME,
}


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


def print_response_headers(r: requests.Response) -> None:
    """
    Print response
    """
    print("Response headers:")
    pprint(dict(r.headers))
    print()


def print_response_text(r: requests.Response) -> None:
    """
    Print response
    """
    print("Response text:")
    pprint(json.loads(r.text))
    print()
