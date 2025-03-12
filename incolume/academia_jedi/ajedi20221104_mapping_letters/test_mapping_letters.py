"""Test module."""

from typing import NoReturn

import pytest
from incolume.academia_jedi.ajedi20221104_mapping_letters.main import (
    mapping_letters,
)


class TestMappingLetters:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                'missíssipi',
                {
                    'm': [0],
                    'i': [1, 7, 9],
                    's': [2, 3, 5, 6],
                    'í': [4],
                    'p': [8],
                },
            ),
            (
                'abracadabra',
                {
                    'a': [0, 3, 5, 7, 10],
                    'b': [1, 8],
                    'r': [2, 9],
                    'c': [4],
                    'd': [6],
                },
            ),
            (
                'açaí',
                {'a': [0, 2], 'ç': [1], 'í': [3]},
            ),
            (
                'água',
                {'á': [0], 'g': [1], 'u': [2], 'a': [3]},
            ),
        ],
    )
    def test_mapping_letters(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert mapping_letters(entrance) == expected
