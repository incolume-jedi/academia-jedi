"""Pagination module.

[Is This a Good Way to deal with API Pagination?](https://www.youtube.com/watch?v=X4WctWZ2ANw).
"""

import logging
from collections.abc import Iterator

import requests
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)
timeout: float = settings.timeout


def data_get(url: str) -> Iterator:
    """Dataget."""
    totals: list = []

    def make_request(url: str, result: list) -> list[str]:
        """Make request."""
        resp = requests.get(url, timeout=timeout)
        logging.debug(url)

        result += resp.json()['results']
        if resp.json()['info']['next'] is None:
            return

        make_request(resp.json()['info']['next'], result)

    make_request(url, totals)
    return totals


def run():
    """Run it."""
    url = 'https://rickandmortyapi.com/api/character?page=1'
    result = data_get(url)
    print(len(result))


if __name__ == '__main__':  # pragma: no cover
    run()
