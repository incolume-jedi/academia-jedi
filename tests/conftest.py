"""Configurate of tests."""
from sys import version_info

import pytest
from tempfile import NamedTemporaryFile
from pathlib import Path


collect_ignore = []


if version_info < (3, 9, 0):  # noqa: UP036
    collect_ignore.extend(
        (
            'incolume/academia_jedi/ajedi20220728_crud_nodb/*.py',
        ),
    )
elif version_info < (3, 10, 0):
    collect_ignore.extend(
        (
            'incolume/academia_jedi/ajedi20220728_crud_nodb',
        ),
    )
elif version_info < (3, 11, 0):
    collect_ignore.extend(
        (
            'incolume/academia_jedi/ajedi20220728_crud_nodb',
        ),
    )
elif version_info < (3, 12, 0):
    collect_ignore.extend(
        (
            'incolume/academia_jedi/ajedi20220728_crud_nodb',
        ),
    )


@pytest.fixture()
def verdade() -> bool:
    """True."""
    return True


@pytest.fixture()
def fakefile() -> Path:
    """Fake file."""
    return Path(NamedTemporaryFile(prefix='academia-jedi-').name)
