import logging
import sys

import pandas as pd
import requests
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover

df = pd.read_csv(
    'https://raw.githubusercontent.com/jhnwr/flask-restful-demo/main/data.csv',
    header=None,
    names=['game_id', 'home_team', 'away_team', 'home_score', 'away_score'],
)


def post_data(item):
    """Post data."""
    headers = {
        'Content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/104.0.5112.102 Safari/537.36',
    }
    payload = item.to_dict()
    try:
        resp = requests.post(
            'http://localhost:5555',
            headers=headers,
            json=payload,
        )
        return resp.json()
    except requests.exceptions.ConnectionError:
        logging.exception(ic(sys.exc_info()))
        sys.exit(1)


for _, values in df.iterrows():
    try:
        print(post_data(values))
    except SystemExit:  # noqa: PERF203
        break
