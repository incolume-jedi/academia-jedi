"""Test iso8601."""

# ruff: noqa: E501

import logging
from icecream import ic
import datetime as dt
import pytest
import pytz
import incolume.academia_jedi.ajedi20221227_datetime_iso8601.handler_datetime_iso8601 as pkg

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


class TestISO8601:
    """Test case."""

    DATE: dt.datetime = dt.datetime(
        1978,
        6,
        20,
        1,
        23,
        45,
        6789,
        pytz.timezone('America/Sao_Paulo'),
    )

    @pytest.fixture()
    def _patch_datetime_now(self, monkeypatch):
        """Fixture."""

        class FakeDateTime(dt.datetime):
            """Class fake datetime."""

            @classmethod
            def now(cls, *args, **kwargs):
                """Method now."""
                ic(args, kwargs)
                return self.DATE

        monkeypatch.setattr(dt, 'datetime', FakeDateTime)

    @pytest.mark.parametrize(
        ['func', 'entrance', 'expected'],
        [
            ('iso8601_format_01', DATE, '1978-06-20T01:23:45.006789-03:06'),
            ('iso8601_format_03', DATE, '1978-06-20T01:23:45.006-03:06'),
            ('iso8601_format_04', DATE, '1978-06-20T01:23:45.006789-0306'),
            ('iso8601_format_05', DATE, '1978-06-20 01:23:45.006789-0306'),
            ('iso8601_format_06', DATE, '1978-06-20T01:23:45.006-03:06'),
            ('iso8601_format_07', DATE, '1978-06-20T01:23:45-03:06'),
        ],
    )
    def test_iso8601(self, func, entrance, expected):
        """Unittest."""
        assert getattr(pkg, func)(entrance) == expected

    @pytest.mark.usefixtures('_patch_datetime_now')
    def test_iso8602_format02(self):
        """Unittest."""
        assert pkg.iso8601_format_02() == '1978-06-20 01:23:45.006-03:06'
