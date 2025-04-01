"""Estudo para Exception group."""

# ruff:noqa: T201

import contextlib
import sys

if sys.version_info < (3, 11):
    with contextlib.suppress(SystemExit):
        sys.exit('This application need Python 3.11+')


def create_eg():
    """Create Exception Group."""
    eg = ExceptionGroup(
        'Exception Group Message!',
        [
            FileNotFoundError("'anime.jpg' not found..."),
            FileNotFoundError("'anime.png' not found..."),
            FileNotFoundError("'icon.ico' not found..."),
            ValueError("'.git' not permited..."),
            ExceptionGroup('Nested exceptions', [ValueError('Not OK!')]),
        ],
    )
    raise eg


if __name__ == '__main__':  # pragma: no cover
    ...
