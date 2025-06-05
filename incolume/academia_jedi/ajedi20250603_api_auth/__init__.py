"""Module for ajedi20250603-api-auth."""

from __future__ import annotations

import base64

import httpx
from icecream import ic

user = 'username'
pw = 'password'


def auth_basic(
    user: str = '',
    pw: str = '',
    url: str = 'https://httpbin.org/basic-auth/{user}/{pw}',
    *,
    update_credentials: bool = False,
) -> httpx.Response:
    """Authenticate using Basic Auth.

    Args:
        user (str): Username for authentication.
        pw (str): Password for authentication.
        url (str): URL for the Basic Auth endpoint, defaulting to
           'https://httpbin.org/basic-auth/{user}/{pw}'.
        update_credentials (bool): If True, use provided user
           and pw; otherwise, use default values.
    """
    user = user or 'username'
    pw = pw or 'password'
    url = (
        url.format(user=user, pw=pw)
        if update_credentials
        else url.format(user='username', pw='password')
    )

    auth_str = base64.b64encode(f'{user}:{pw}'.encode()).decode()

    ic(auth_str)
    headers = {'Authorization': f'Basic {auth_str}'}

    response = httpx.get(url, headers=headers)
    response.raise_for_status()  # Ensure we raise an error for bad responses
    ic(response.json())
    return response


def main() -> None:
    """Main function for ajedi20250603-api-auth."""
    print('Hello from ajedi20250603-api-auth!')  # noqa: T201
    auth_basic()  # Replace with actual credentials
    auth_basic('figueredo', 'pudim')  # Print the JSON response for debugging


if __name__ == '__main__':
    main()
