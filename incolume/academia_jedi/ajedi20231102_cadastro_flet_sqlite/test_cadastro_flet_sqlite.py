"""Unittests."""
import logging
from os import environ, getenv
from pathlib import Path
from tempfile import NamedTemporaryFile

from incolume.academia_jedi.\
    ajedi20231102_cadastro_flet_sqlite.database import (
    get_connection,
)


def test_get_connection_forma1(caplog) -> None:
    """Test get_connection forma1."""
    with (
        Path(NamedTemporaryFile().name) as file,
        caplog.at_level(logging.DEBUG),
    ):
        get_connection(file)
        assert file.as_posix() in caplog.text


def test_get_connection_forma2(caplog) -> None:
    """Test get_connection forma2."""
    with (
        Path(NamedTemporaryFile().name) as file,
        caplog.at_level(logging.DEBUG),
    ):
        environ['APP_INCOLUME_DB'] = file.as_posix()
        get_connection()
        assert (
            getenv('APP_INCOLUME_DB') in caplog.text
            and getenv('APP_INCOLUME_DB') == file.as_posix()
        )


def test_get_connection_forma3(caplog) -> None:
    """Test get_connection forma3."""
    del environ['APP_INCOLUME_DB']

    with caplog.at_level(logging.DEBUG):
        get_connection()
        assert 'db/cad.db' in caplog.text
