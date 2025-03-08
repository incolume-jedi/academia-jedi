"""Submodule test."""

from typing import NoReturn
import pytest


class TestAdedonha:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', '', marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert entrance == expected
