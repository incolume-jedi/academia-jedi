"""Configurate of tests."""

from __future__ import annotations

import logging
from pathlib import Path
from sys import version_info
from tempfile import NamedTemporaryFile

import pytest
from icecream import ic

# ruff: noqa: UP036

collect_ignore = ['setup.py', '__main__.py']


if version_info < (3, 9, 0):
    logging.info(ic('Does not run on python below 3.9'))
    files = []
    files.extend(
        Path('incolume/academia_jedi/ajedi20220728_crud_nodb/').rglob(
            'test_*.py',
        ),
    )
    files.extend(
        Path('incolume/academia_jedi/ajedi20220728_crud_nodb/').rglob(
            '*test*.py',
        ),
    )
    logging.debug(ic(files))
    collect_ignore.extend(files)

if version_info < (3, 10, 0):
    logging.info(ic('Does not run on python below 3.10'))
    files = []
    files.extend(
        Path('incolume/academia_jedi/ajedi20240408_dundler_methods/').rglob(
            '*test*.py',
        ),
    )
    logging.debug(ic(files))
    collect_ignore.extend(files)

if version_info < (3, 11, 0):
    logging.info(ic('Does not run on python below 3.11'))
    path = Path('incolume/academia_jedi/ajedi20221104_collections_deque')
    files = []
    files.extend(path.rglob('*tests*.py'))
    files.extend(
        Path(
            'incolume/academia_jedi/ajedi20221219_Como_Usar_ExceptionsGroups',
        ).rglob('*.py'),
    )
    logging.debug(ic(files))
    collect_ignore.extend(files)

if version_info < (3, 12, 0):
    logging.info(ic('Does not run on python below 3.12'))
    collect_ignore.append(
        r'incolume/academia_jedi/ajedi20250224_estudo_itertools_batched/test_20250224.py',
    )

if version_info < (3, 13, 0):
    logging.info(ic('Does not run on python below 3.13'))

if version_info < (3, 14, 0):
    logging.info(ic('Does not run on python below 3.14'))

if version_info < (3, 15, 0):
    logging.info(ic('Does not run on python below 3.15'))

if version_info < (4, 0, 0):
    logging.info(ic('Does not run on python below 4.0'))
    files = [
        r'incolume/academia_jedi/ajedi20231213_aspose_pkg/test_aspose.py',
    ]
    collect_ignore.extend(files)

logging.debug(ic(collect_ignore))


@pytest.fixture()
def verdade() -> bool:
    """True."""
    return True


@pytest.fixture()
def fakefile() -> Path:
    """Fake file."""
    return Path(NamedTemporaryFile(prefix='academia-jedi-').name)
