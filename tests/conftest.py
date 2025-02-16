"""Configurate of tests."""

import logging
from pathlib import Path
from sys import version_info
from tempfile import NamedTemporaryFile

import pytest
from icecream import ic

collect_ignore = []


if version_info < (3, 9, 0):  # noqa: UP036
    collect_ignore.extend([
        r'incolume/academia_jedi/ajedi20220728_crud_nodb/*',
    ])
if version_info < (3, 10, 0):  # noqa: UP036
    collect_ignore.extend([
        r'incolume/academia_jedi/ajedi20240408_dundler_methods/*',
    ])
if version_info < (3, 11, 0):
    pass

if version_info < (3, 12, 0):
    pass

if version_info < (4, 0, 0):
    collect_ignore.append(
        r'incolume/academia_jedi/ajedi20231213_aspose_pkg/test_aspose.py',
    )

logging.debug(ic(collect_ignore))


@pytest.fixture()
def verdade() -> bool:
    """True."""
    return True


@pytest.fixture()
def fakefile() -> Path:
    """Fake file."""
    return Path(NamedTemporaryFile(prefix='academia-jedi-').name)
