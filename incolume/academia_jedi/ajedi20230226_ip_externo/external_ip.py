"""Baseado em https://www.youtube.com/watch?v=jF3_g8eDeEo"""

import re
from urllib.request import urlopen
import logging

__author__ = "@britodfbr"  # pragma: no cover
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def get_ip():
    req = urlopen("http://checkip.dyndns.com/")  # necessário API
    logging.debug(type(req))
    data = str(req.read())
    logging.debug(data)
    logging.debug(type(data))

    ip = re.search(r"(\d+(\.\d+){3})", data).group()
    logging.debug(ip)
    return ip


def run():
    print(get_ip())


if __name__ == "__main__":  # pragma: no cover
    run()
