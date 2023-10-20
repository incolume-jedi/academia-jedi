import logging
from datetime import datetime

import pytz
from handler_datetime import (
    iso8601_format_01,
    iso8601_format_02,
    iso8601_format_03,
    iso8601_format_04,
    iso8601_format_05,
    iso8601_format_06,
    iso8601_format_07,
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)
DATE = datetime(
    1978, 6, 20, 1, 23, 45, 6789, pytz.timezone('America/Sao_Paulo')
)


def run():
    print(
        iso8601_format_01(DATE),
        iso8601_format_02(),
        iso8601_format_03(DATE),
        iso8601_format_04(DATE),
        iso8601_format_05(DATE),
        iso8601_format_06(DATE),
        iso8601_format_07(DATE),
        sep='\n',
    )


if __name__ == '__main__':  # pragma: no cover
    run()
