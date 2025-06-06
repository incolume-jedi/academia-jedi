"""Module to access OpenWeatherMap API."""

import httpx
from icecream import ic
try:
    from config import settings
except (ImportError, ModuleNotFoundError):
    from dotenv import load_dotenv
    import os
    load_dotenv()



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
        'appid': token or os.getenv('OPEN_WEATHER_MAP_API_KEY'),
        'q': city or 'Brasília',
        'units': 'metric',
    }
    response = httpx.get(url, params=params)
    # response.raise_for_status()  # Ensure we raise an error for bad responses
    # ic(response.json())
    return response


def main():
    """Main function to run the OpenWeatherMap access module."""
    print('Hello from ajedi20250606-acesso-openweather!')  # noqa: T201


if __name__ == '__main__':
    main()
