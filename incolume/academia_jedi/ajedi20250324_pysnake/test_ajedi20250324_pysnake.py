"""Test module."""

from typing import NoReturn
import pytest
import incolume.academia_jedi.ajedi20250324_pysnake as mypysnake


class TestMyPySnake:
    """Test cases."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            (mypysnake.Personagem(), {'col': 15, 'lin': 10}),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Test unit."""
        assert entrance.__dict__ == expected
