"""[Is This a Good Way to deal with API Pagination?]
(https://www.youtube.com/watch?v=X4WctWZ2ANw).
"""
import logging
from collections.abc import Iterator

import requests

__author__ = '@britodfbr'  # pragma: no cover
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def data_get(url: str) -> Iterator:
    """"""
    totals = []

    def make_request(url: str):
        resp = requests.get(url)
        print(url)

        for item in resp.json()['results']:
            totals.append(item)

        if resp.json()['info']['next'] is None:
            return

        make_request(resp.json()['info']['next'])

    make_request(url)
    return totals


def run():
    url = 'https://rickandmortyapi.com/api/character?page=1'
    print(len(data_get(url)))


if __name__ == '__main__':  # pragma: no cover
    run()
