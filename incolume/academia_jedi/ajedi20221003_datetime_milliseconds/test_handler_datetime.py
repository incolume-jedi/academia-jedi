import re

# ruff: noqa: D100, D101

import incolume.academia_jedi.ajedi20221003_datetime_milliseconds as pkg
from incolume.academia_jedi import logger
from icecream import ic


__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    def test_example01(self, capsys):
        """Test example01."""
        pkg.example01()
        stream, err = capsys.readouterr()
        logger.error(ic(err))
        assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', stream)

    def test_example02(self, capsys):
        """Test example02."""
        pkg.example02()
        stream, err = capsys.readouterr()
        logger.error(ic(err))
        assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', stream)

    def test_example03(self, capsys):
        """Test example03."""
        pkg.example03()
        stream, err = capsys.readouterr()
        logger.error(ic(err))
        assert re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', stream)
