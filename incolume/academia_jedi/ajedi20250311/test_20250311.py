"""Test module."""

from typing import NoReturn
import incolume.academia_jedi.ajedi20250311 as pkg

class TestCountVowel:
    """Test case."""
    def test_0(self, monkeypatch) -> NoReturn:
        """Unittest."""
        monkeypatch.setattr(
            'httpx.get',
            lambda _: pkg.httpx.Response(200, text=pkg.content),
        )
        assert pkg.get_text()


    def test_1(self) -> NoReturn:
        """Unittest."""
        assert pkg.count_vowels(pkg.content) == {
            'a': 168,
            'e': 138,
            'i': 118,
            'o': 159,
            'u': 54,
        }
