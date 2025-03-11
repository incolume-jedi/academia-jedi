"""Subpackage."""

import httpx
from bs4 import BeautifulSoup
from icecream import ic

url: str = 'https://pt.wikipedia.org/wiki/Python'




def get_text():
    """Get text."""
    resp = httpx.get(url)
    ic(resp)
    soup = BeautifulSoup(resp.content, 'html5lib')
    # ic(soup.select('a'))
