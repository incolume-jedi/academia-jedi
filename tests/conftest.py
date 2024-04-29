"""Configurate of tests."""

from pathlib import Path
from sys import version_info
from tempfile import NamedTemporaryFile

import pytest

collect_ignore = []


if version_info < (3, 9, 0):  # noqa: UP036
    collect_ignore.extend(
        ('incolume/academia_jedi/ajedi20220728_crud_nodb/*.py',),
    )
elif version_info < (3, 10, 0):
    collect_ignore.extend(
        ('incolume/academia_jedi/ajedi20240408_dundler_methods/*',),
    )
elif version_info < (3, 11, 0) or version_info < (3, 12, 0):
    collect_ignore.extend(
        (
            'incolume/academia_jedi/ajedi20220728_crud_nodb',
            'incolume/academia_jedi/ajedi20240408_dundler_methods/*',
        ),
    )
elif version_info < (4, 0, 0):
    collect_ignore.extend(
        ('incolume\academia_jedi\ajedi20231213_aspose_pkg\test_aspose.py'),
    )


@pytest.fixture()
def verdade() -> bool:
    """True."""
    return True


@pytest.fixture()
def fakefile() -> Path:
    """Fake file."""
    return Path(NamedTemporaryFile(prefix='academia-jedi-').name)
