# !/usr/bin/env python
import pandas as pd
import requests
from bs4 import BeautifulSoup

__author__ = '@britodfbr'  # pragma: no cover
url = 'https://free-proxy-list.net/'


def run():
    rq = requests.get(url)
    soup = BeautifulSoup(rq.content, 'html.parser')
    df = pd.read_html(soup.prettify())[0]
    print(df)


if __name__ == '__main__':  # pragma: no cover
    run()
