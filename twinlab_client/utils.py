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

# Number of sigmas corresponding to Gaussian probability mass
# in 0.05 intervals from 0.05 to 0.95
NSIGS = [
    0.06270677794321385,
    0.12566134685507416,
    0.18911842627279238,
    0.2533471031357997,
    0.31863936396437514,
    0.38532046640756773,
    0.45376219016987956,
    0.5244005127080407,
    0.5977601260424784,
    0.6744897501960817,
    0.7554150263604693,
    0.8416212335729143,
    0.9345892910734803,
    1.0364333894937898,
    1.1503493803760079,
    1.2815515655446004,
    1.4395314709384563,
    1.6448536269514733,
    1.959963984540056,
]


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


def check_response(r: requests.Response) -> None:
    if r.status_code != 200:
        print("Status code:", r.status_code)
        print_response_text(r)
        raise RuntimeError("Response error")
