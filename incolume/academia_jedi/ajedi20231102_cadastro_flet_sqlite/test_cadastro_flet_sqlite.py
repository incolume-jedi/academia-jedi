"""Unittests."""
import logging
from os import environ, getenv
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from incolume.academia_jedi.\
    ajedi20231102_cadastro_flet_sqlite.database import (
    get_connection,
)


@pytest.fixture()
def tmpfile() -> Path:
    """Return a tempfile."""
    return Path(NamedTemporaryFile().name)


def test_get_connection_forma1(caplog, tmpfile) -> None:
    """Test get_connection forma1."""
    with tmpfile, caplog.at_level(logging.DEBUG):
        get_connection(tmpfile)
        assert tmpfile.as_posix() in caplog.text


def test_get_connection_forma2(caplog, tmpfile) -> None:
    """Test get_connection forma2."""
    with tmpfile, caplog.at_level(logging.DEBUG):
        environ['APP_INCOLUME_DB'] = tmpfile.as_posix()
        get_connection()
        assert (
            getenv('APP_INCOLUME_DB') in caplog.text
            and getenv('APP_INCOLUME_DB') == tmpfile.as_posix()
        )


def test_get_connection_forma3(caplog) -> None:
    """Test get_connection forma3."""
    del environ['APP_INCOLUME_DB']

    with caplog.at_level(logging.DEBUG):
        get_connection()
        assert 'db/cad.db' in caplog.text
