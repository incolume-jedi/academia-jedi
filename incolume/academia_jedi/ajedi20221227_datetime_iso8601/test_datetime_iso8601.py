import logging

from datetime import datetime

import pytz
import incolume.academia_jedi.ajedi20221227_datetime_iso8601.handler_datetime_iso8601 as pkg

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)
class TestISO8601:
    """Test case."""
    DATE: datetime = datetime(
    1978,
    6,
    20,
    1,
    23,
    45,
    6789,
    pytz.timezone('America/Sao_Paulo'),
)

    pytest.mark.parametrize(
        'func entrance expected'.split(),
        [
        ('iso8601_format_01', DATE, ''),
        ('iso8601_format_02', None, ''),
        ('iso8601_format_03', DATE, ''),
        ('iso8601_format_04', DATE, ''),
        ('iso8601_format_05', DATE, ''),
        ('iso8601_format_06', DATE, ''),
        ('iso8601_format_07', DATE, ''),
        ],
    )
    def test_iso8601(self, func, entrance, expected):
        """Unittest."""
        assert getattr(pkg, func)(entrance) == expected
