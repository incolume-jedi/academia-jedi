"""Module initialyzer."""

import logging
from pathlib import Path

import requests
from tomli import load

config: Path = Path(__file__).parent / 'conf.toml'
timeout: float = 1.5

with config.open('rb') as file:
    url: str = load(file)['url']['toscrape']

logging.debug(url)

resp: requests.Response = requests.get(url=url, timeout=timeout)
logging.debug(resp)
