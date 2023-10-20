import logging
import re
import typing
import urllib.request

import httpx
import requests
import urllib3.connection

__author__ = '@britodfbr'  # pragma: no cover
URL: typing.Final[str] = 'http://checkip.dyndns.com'


def tratativa1():
    """Get external IP with urllib."""
    try:
        req = urllib.request.urlopen(URL)
        logging.debug(req)
        data = str(req.read())
        ip = re.search(r'(\d+(\.\d+){3})', data).group()
        logging.debug(ip)
        return ip
    except Exception as e:
        logging.error('{}:{}', e.__class__.__name__, e)
        print(e)


def tratativa2():
    """Get external IP with urllib3."""
    try:
        clientweb = urllib3.PoolManager()
        req = clientweb.request('GET', URL)
        logging.debug(req.status)
        logging.debug(req.data)
        data = str(req.data)
        ip = re.search(r'(\d+(\.\d+){3})', data).group()
        logging.debug(ip)
        return ip
    except Exception as e:
        logging.error('{}:{}', e.__class__.__name__, e)
        print(e)


def tratativa3():
    """Get external IP with requests."""
    try:
        req = requests.get(URL)
        logging.debug(req.status_code)
        ip = re.search(r'(\d+(\.\d+){3})', req.text).group()
        logging.debug(ip)
        return ip
    except Exception as e:
        logging.error('{}:{}', e.__class__.__name__, e)
        print(e)


def tratativa4():
    """Get external IP with httpx."""
    try:
        req = httpx.get(URL)
        logging.debug(req.status_code)

        ip = re.search(r'(\d+(\.\d+){3})', req.text).group()
        logging.debug(ip)
        return ip

    except Exception as e:
        logging.error('{}:{}', e.__class__.__name__, e)
        print(e)


def run():
    """Running it."""
    functions: typing.List[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print('    >>> {}'.format(func.__doc__))
        try:
            if result := func():
                print(result)
        except ValueError as e:
            logging.error(f'{e.__class__.__name__}: {e}')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
