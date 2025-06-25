"""Module for ajedi20250603-api-auth."""

from __future__ import annotations

import base64
import os
from pathlib import Path

import httpx
from config import settings
from dotenv import load_dotenv
from icecream import ic

load_dotenv(Path(__file__).parent / 'dotenv')
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


def auth_token(
    city: str = '',
    token: str = '',
    url: str = 'https://api.openweathermap.org/data/2.5/weather',
) -> httpx.Response:
    """Authenticate using a token.

    Args:
        city (str): City name for the weather query, defaulting to 'Brasília'.
        token (str): API token for OpenWeatherMap.
        url (str): URL for the OpenWeatherMap API endpoint.
    """
    params = {
        'appid': token or settings.OPEN_WEATHER_MAP_API_KEY,
        'q': city or 'Brasília',
        'units': 'metric',
    }
    response = httpx.get(url, params=params)
    response.raise_for_status()  # Ensure we raise an error for bad responses
    ic(response.json())
    return response


def get_bearer(
    user_id: str = '',
    user_pw: str = '',
    url: str = '',
) -> httpx.Response:
    """Authenticate using Bearer token.

    Args:
        url (str): URL for the Bearer token endpoint.
        user_id (str): Client ID for Spotify API.
        user_pw (str): Client Secret for Spotify API.

    Returns:
        httpx.Response: Response object containing the result of the request.

    hiyik95265@jio1.com:MDjrJEHJTnVfbE2
    """
    url = url or 'https://accounts.spotify.com/api/token'
    user_id = user_id or os.environ.get('SPOTIFY_CLIENT_ID')
    user_pw = user_pw or os.environ.get('SPOTIFY_CLIENT_SECRET')

    body = {
        'grant_type': 'client_credentials',
    }
    response = httpx.post(
        url,
        data=body,
        auth=httpx.BasicAuth(user_id, user_pw),
    )
    response.raise_for_status()  # Ensure we raise an error for bad responses
    ic(response.json())
    return response


def get_spotify(**kwargs: str) -> httpx.Response:
    """Get Spotify data using Bearer token authentication.

    Args:
        **kwargs: Additional keyword arguments for the request.
    """
    headers = {
        'Content-Type': 'application/json',
    }
    url = kwargs.get('url', 'https://api.spotify.com/v1/artists/{id}')
    artist_id = kwargs.get('artist_id')
    token = kwargs.get('token')

    if token:
        headers['Authorization'] = f'Bearer {token}'

    response = httpx.get(url=url.format(id=artist_id), headers=headers)
    ic(response.json())
    return response


def main() -> None:
    """Main function for ajedi20250603-api-auth."""
    print('Hello from ajedi20250603-api-auth!')
    try:
        auth_basic()  # Replace with actual credentials
    except httpx.HTTPStatusError as e:
        ic(f'HTTP error occurred: {e}')

    try:
        auth_basic(
            'figueredo',
            'pudim',
        )  # Print the JSON response for debugging
    except httpx.HTTPStatusError as e:
        ic(f'HTTP error occurred: {e}')

    try:
        get_spotify(artist_id='0gO5Vbklho8yrBrUdHhuLH')
    except httpx.HTTPStatusError as e:
        ic(f'HTTP error occurred: {e}')

    try:
        access_token = get_bearer().json()
        get_spotify(
            token=access_token.get('access_token'),
            artist_id='0gO5Vbklho8yrBrUdHhuLH',
        )
    except httpx.HTTPStatusError as e:
        ic(f'HTTP error occurred: {e}')


if __name__ == '__main__':
    main()
