"""Test module."""

from typing import NoReturn

import pytest
import incolume.academia_jedi.ajedi20250311.count_vowel as pkg
import incolume.academia_jedi.ajedi20250311.cesar_cifer as cc


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

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({}, ''),
            ({'text': 'abcd'}, 'abcd'),
            ({'text': 'abcd', 'key': 1}, 'bcde'),
            ({'text': 'ada', 'key': 2}, 'cfc'),
            ({'text': 'ada', 'key': -2}, 'yby'),
            ({'text': 'açaí', 'key': 13}, 'nçní'),
            ({'text': 'água de açaí', 'key': -13}, 'áthn qr nçní'),
        ],
    )
    def test_cesar_cifer(self, entrance, expected):
        """Unittest."""
        assert cc.cesar_cifer(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('abc', 'nop'),
            ('', ''),
        ],
    )
    def test_rot13(self, entrance, expected):
        """Unittest."""
        assert cc.rot13a(entrance) == expected
