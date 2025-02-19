"""Configurate of tests."""

from __future__ import annotations

import logging
from pathlib import Path
from sys import version_info
from tempfile import NamedTemporaryFile

import pytest
from icecream import ic

# ruff: noqa: UP036

collect_ignore = ['main.py', 'setup.py']


if version_info < (3, 9, 0):
    logging.debug(
        ic([
            collect_ignore.append(file)
            for file in Path(
                'incolume/academia_jedi/ajedi20220728_crud_nodb/',
            ).rglob('*.py')
        ]),
    )

if version_info < (3, 10, 0):
    logging.debug(
        ic([
            collect_ignore.append(file)
            for file in Path(
                'incolume/academia_jedi/ajedi20240408_dundler_methods/',
            ).rglob('*.py')
        ]),
    )

if version_info < (3, 11, 0):
    logging.debug(
        ic([
            collect_ignore.append(file)
            for file in Path(
                'incolume/academia_jedi/ajedi20221104_collections_deque',
            ).rglob('*.py')
        ]),
    )

if version_info < (3, 12, 0):
    collect_ignore.append(
        r'incolume/academia_jedi/ajedi20250224_estudo_itertools_batched/test_20250224.py',
    logging.debug(
        ic([
            collect_ignore.append(file)
            for file in Path(
                'incolume/academia_jedi/ajedi20231101_handler_docx',
            ).rglob('*.py')
        ]),
    )


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
