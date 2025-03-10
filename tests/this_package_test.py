"""Test package."""

from typing import NoReturn

import pytest
import incolume.academia_jedi as pkg


class TestPackage:
    """Test for test this package."""

    @pytest.mark.parametrize(
        'entrance',
        [
            'format_log',
            'format_log_win',
        ],
    )
    def test_load_envvar(self, entrance) -> NoReturn:
        """Unittest."""
        assert getattr(pkg.settings, entrance) == ''
