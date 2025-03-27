"""Test for Module."""

import re
from pathlib import Path

import pytest

from incolume.academia_jedi import __version__, load
from config import settings

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize('entrance expected'.split(), [(__version__, True)])
def test_semver(entrance, expected):
    """Test for semantic versioning.

    :param entrance: entrance parameter
    :param expected: expected parameter
    :return: assert result
    """
    assert (
        bool(
            re.fullmatch(
                settings.semver,
                entrance,
                flags=re.I,
            ),
        )
        == expected
    )


def test_version():
    """Test version."""
    with (
        Path(__file__)
        .parents[1]
        .joinpath('pyproject.toml')
        .open(
            'rb',
        ) as file
    ):
        assert __version__ == load(file)['tool']['poetry']['version']
