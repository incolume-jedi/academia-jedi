# !/usr/bin/env python
"""Proxy with python."""
import requests

__author__ = '@britodfbr'  # pragma: no cover
# urls
urls = ('https://httpbin.org/ip',)
# proxies from https://free-proxy-list.net/
proxies_list = [
    '193.122.71.184:3128',
    '198.59.191.234:8080',
    '45.42.177.49:3128',
    '49.0.2.242:8090',
    '8.219.97.248:80',
    '8.211.22.130:5678',
]


def no_proxy_access():
    r = requests.get(urls[0])
    print(f'{r.status_code=}, {r.json()=}')


def with_proxy_01():
    r = requests.get(
        urls[0],
        proxies={'http': proxies_list[0], 'https': proxies_list[0]},
        timeout=3,
    )
    print(f'{r.status_code=}, {r.json()=}')


def run():
    no_proxy_access()
    with_proxy_01()


if __name__ == '__main__':  # pragma: no cover
    run()
