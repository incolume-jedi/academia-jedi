"""Module to access OpenWeatherMap API."""

import httpx
from icecream import ic

try:
    from config import settings

    token_api = settings.OPEN_WEATHER_MAP_API_KEY
except (ImportError, ModuleNotFoundError):
    import os

    from dotenv import load_dotenv

    load_dotenv()
    token_api = os.getenv('OPEN_WEATHER_MAP_API_KEY')


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
        'appid': token or token_api,
        'q': city or 'Brasília',
        'units': 'metric',
        'lang': 'pt_br',
    }
    response = httpx.get(url, params=params)
    ic(response.json())
    return response


def info():
    """Main function to run the OpenWeatherMap access module."""
    print('Hello from ajedi20250606-acesso-openweather!')  # noqa: T201


if __name__ == '__main__':
    info()
