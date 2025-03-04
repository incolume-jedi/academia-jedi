"""Test module."""

from typing import NoReturn
import pytest


class TestCase:
    """Testcase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', '', marks=[]),
            pytest.param('', '', marks=[pytest.mark.skip]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Test 0."""
        assert entrance == expected
