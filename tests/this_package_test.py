"""Test package."""

from typing import NoReturn

import pytest
import incolume.academia_jedi as pkg


class TestPackage:
    """Test for test this package."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'format_log',
                r'%(asctime)s;%(levelname)-8s;%(name)s;%(module)s;%(funcName)s;%(message)s',
                marks=[],
            ),
            pytest.param(
                'format_log_win',
                r'$(asctime)s;$(levelname)-8s;$(name)s;$(module)s;$(funcName)s;$(message)s',
                marks=[],
            ),
            pytest.param('msg', 'Hello Dev', marks=[]),
            pytest.param('tz', 'America/Sao_Paulo', marks=[]),
            pytest.param('blue', '#0060B5', marks=[]),
        ],
    )
    def test_load_envvar(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert getattr(pkg.settings, entrance) == expected
