from typing import Optional
import os
import json
from dotenv import load_dotenv

import requests

# Load environment variables
load_dotenv(override=True)  # NOTE: Override seems to be necessary
TWINLAB_SERVER: str = os.getenv("TWINLAB_SERVER")
if not TWINLAB_SERVER:
    raise ValueError("TWINLAB_SERVER not set in .env")

### Helper functions ###


def _create_headers(content_type: Optional[str] = None, verbose=False) -> dict:
    headers = {}
    if "rapidapi" in TWINLAB_SERVER:
        headers = {
            "X-RapidAPI-Key": os.getenv("TWINLAB_KEY"),
            "X-RapidAPI-Host": os.getenv("TWINLAB_HOST"),
        }
    else:
        headers = {
            "X-RapidAPI-Proxy-Secret": os.getenv("TWINLAB_SECRET"),
            "X-RapidAPI-User": os.getenv("TWINLAB_USERNAME"),
        }
    if content_type:
        headers["Content-Type"] = content_type
    if verbose:
        headers["X-Verbose"] = "true"
    return headers


def _parse_response(response: requests.Response) -> dict | str:
    # TODO: Use atttribute of response to check if json/text
    try:
        return response.json()
    except:
        return response.text

###  ###

### API ###


def get_user(verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/user"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def get_versions(verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/versions"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def generate_upload_url(dataset_id: str, verbose=False) -> str:
    url = f"{TWINLAB_SERVER}/upload_url/{dataset_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def process_uploaded_dataset(dataset_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/datasets/{dataset_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.post(url, headers=headers)
    body = _parse_response(response)
    return body


def upload_dataset(data_csv: str, dataset_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/datasets/{dataset_id}"
    headers = _create_headers("text/plain", verbose=verbose)
    response = requests.put(url, headers=headers, data=data_csv)
    body = _parse_response(response)
    return body


def list_datasets(verbose=False) -> list:
    url = f"{TWINLAB_SERVER}/datasets"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def view_dataset(dataset_id: str, verbose=False) -> str:
    url = f"{TWINLAB_SERVER}/datasets/{dataset_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def summarise_dataset(dataset_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/datasets/{dataset_id}/summarise"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def delete_dataset(dataset_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/datasets/{dataset_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.delete(url, headers=headers)
    body = _parse_response(response)
    return body


def train_model(parameters_json: str, model_id: str, processor: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/models/{model_id}"
    headers = _create_headers("application/json", verbose=verbose)
    headers["X-Processor"] = processor
    training_parameters = json.loads(parameters_json)
    response = requests.put(url, headers=headers, json=training_parameters)
    body = _parse_response(response)
    return body


def list_models(verbose=False) -> list:
    url = f"{TWINLAB_SERVER}/models"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def status_model(model_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/models/{model_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def summarise_model(model_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/models/{model_id}/summarise"
    headers = _create_headers(verbose=verbose)
    response = requests.get(url, headers=headers)
    body = _parse_response(response)
    return body


def use_model(eval_csv: str, model_id: str, method: str, processor: str, verbose=False) -> str:
    url = f"{TWINLAB_SERVER}/models/{model_id}/{method}"
    headers = _create_headers("text/plain", verbose=verbose)
    headers["X-Processor"] = processor
    response = requests.post(url, headers=headers, data=eval_csv)
    body = _parse_response(response)
    return body


def delete_model(model_id: str, verbose=False) -> dict:
    url = f"{TWINLAB_SERVER}/models/{model_id}"
    headers = _create_headers(verbose=verbose)
    response = requests.delete(url, headers=headers)
    body = _parse_response(response)
    return body

### ###
