"""Acesso API com Python."""

from __future__ import annotations

from pathlib import Path

import requests
from config import settings
from icecream import ic

url = 'https://httpbin.org'

data = {
    'project': 'academia_jedi',
    'version': '0.116.0',
    'author': 'Incolume',
    'author_email': 'dev@incolume.com.br',
    'subproject': {
        'namespace': 'ajedi20250601-python-api',
        'version': '0.1.0',
        'author': 'Brito',
        'author_email': 'britodfbr@gmail.com',
        'description': 'Acesso API com Python',
        'license': 'MIT',
    },
    'sequence': [1, 2, 3, 4, 5],
}

params = {
    'data-inicial': '2023-06-01',
    'data-final': '2023-06-30',
}


def get_api_response(timeout: int = 0) -> requests.Response:
    """Get the response from the API."""
    timeout = timeout or max(settings.timeout, 1)
    response = requests.get(f'{url}/get', timeout=timeout)
    response.raise_for_status()  # Raise an error for bad responses
    return response


def post_api_response(data: dict, timeout: int = 0) -> requests.Response:
    """Post data to the API and get the response.

    Args:
        data (dict): The data to post to the API.
        timeout (int): The timeout for the request in seconds. Defaults to 0.
    """
    timeout = max(timeout, 1)
    response = requests.post(f'{url}/post', timeout=timeout, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    return response


def new_post_api_response(**kwargs: str) -> requests.Response:
    """Post data to the API and get the response.

    Args:
        data (dict): The data to post to the API.
        timeout (int): The timeout for the request in seconds. Defaults to 1.
        kwargs: Additional keyword arguments to pass to the request.
    """
    timeout = max(kwargs.pop('timeout'), 1)

    response = requests.post(f'{url}/post', timeout=timeout, **kwargs)
    response.raise_for_status()  # Raise an error for bad responses
    return response


def main() -> None:
    """Main function to run the API example."""
    print('Hello from ajedi20250601-python-api!')  # noqa: T201
    resp1 = get_api_response()
    ic(resp1.json())

    resp2 = post_api_response(data, timeout=5)
    ic(resp2.json())

    resp3 = new_post_api_response(data=data, params=params, timeout=5)
    ic(resp3.json())
    ic(resp3.request.url)

    ic((Path(__file__).parents[2] / 'data_files').exists())


if __name__ == '__main__':
    main()
