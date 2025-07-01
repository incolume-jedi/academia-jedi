"""Monkeypatching functions."""

from __future__ import annotations

from pathlib import Path

import httpx
import requests
from icecream import ic


def getssh():
    """Simple function to return expanded homedir ssh path."""
    return ic(Path.home() / '.ssh')


def get_uuid(url: str = '') -> httpx.Response:
    """Get uuid from httpbin.org."""
    url = url or 'http://httpbin.org/uuid'

    return ic(httpx.get(url).json())


def get_uid(url: str = '') -> requests.Response:
    """Get uuid from httpbin.org."""
    url = url or 'http://httpbin.org/uuid'

    return ic(requests.get(url, timeout=30).json())


def run():
    """Run it."""
    getssh()
    get_uuid()


if __name__ == '__main__':
    run()
