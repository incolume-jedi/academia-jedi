"""Configurate of tests."""

from __future__ import annotations

import logging
from pathlib import Path
from sys import version_info
from tempfile import NamedTemporaryFile

import pytest
from icecream import ic

collect_ignore = ['setup.py']


if version_info < (3, 9, 0):  # noqa: UP036
    files = Path('incolume/academia_jedi/ajedi20220728_crud_nodb/').rglob(
        '*.py',
    )
    logging.debug(ic([collect_ignore.append(file) for file in files]))

if version_info < (3, 10, 0):
    files = Path(
        'incolume/academia_jedi/ajedi20240408_dundler_methods/',
    ).rglob('*.py')
    logging.debug(ic([collect_ignore.append(file) for file in files]))

if version_info < (3, 11, 0):
    path = Path('incolume/academia_jedi/ajedi20221104_collections_deque')
    files = path.rglob('*.py')
    logging.debug(ic([collect_ignore.append(file) for file in files]))

if version_info < (3, 12, 0):
    collect_ignore.append(
        r'incolume/academia_jedi/ajedi20250224_estudo_itertools_batched/test_20250224.py',
    )

if version_info < (3, 13, 0):
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
