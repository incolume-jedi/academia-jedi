"""Module for ajedi20250603-api-auth."""

from __future__ import annotations

import base64

import httpx
from icecream import ic

user = 'username'
pw = 'password'

url = 'https://httpbin.org/basic-auth/{user}/{pw}'


def authenticate(
    user: str = '',
    pw: str = '',
    url: str = url,
) -> httpx.Response:
    """Authenticate using Basic Auth."""
    user = user or 'username'
    pw = pw or 'password'

    auth_str = base64.b64encode(f'{user}:{pw}'.encode()).decode()

    ic(auth_str)

    headers = {'Authorization': f'Basic {auth_str}'}

    response = httpx.get(url.format(user=user, pw=pw), headers=headers)
    response.raise_for_status()  # Ensure we raise an error for bad responses
    ic(response)
    return response


def main() -> None:
    """Main function for ajedi20250603-api-auth."""
    print('Hello from ajedi20250603-api-auth!')  # noqa: T201
    authenticate()  # Replace with actual credentials
    authenticate().json()  # Print the JSON response for debugging


if __name__ == '__main__':
    main()
