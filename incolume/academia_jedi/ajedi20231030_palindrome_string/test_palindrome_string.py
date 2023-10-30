"""Teste academia 20231030."""


import pytest

from incolume.academia_jedi.ajedi20231030_palindrome_string.\
palindrome_string import (
    is_palindrome,
)


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('Python', False),
        ('anna', True),
        ('walter', False),
        (12321, True),
        (123456, False),
        ('ada', True),
        ('aibofobia', True),
        ('A base do teto desaba', True),
        ('A cara rajada da jararaca', True),
        ('Socorram-me, subi no ônibus em Marrocos', True),
        ('Me vê se a panela da moça é de aço, Madalena Paes, e vem', True),
    ],
)
def test_is_palindrome(entrance, expected) -> None:
    """Testar função palindrome."""
    assert is_palindrome(entrance) == expected
