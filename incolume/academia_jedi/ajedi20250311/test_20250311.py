"""Test module."""

from typing import NoReturn

import pytest
import incolume.academia_jedi.ajedi20250311.count_vowel as pkg


class TestCountVowel:
    """Test case."""

    def test_0(self, monkeypatch) -> NoReturn:
        """Unittest."""
        monkeypatch.setattr(
            'httpx.get',
            lambda _: pkg.httpx.Response(200, text=pkg.content),
        )
        assert pkg.get_text()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('a', 189),
            pytest.param('e', 146),
            pytest.param('i', 126),
            pytest.param('o', 166),
            pytest.param('u', 55),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.count_vowels(pkg.content).get(entrance) == expected


class TestCesarCifer:
    """Test case."""
