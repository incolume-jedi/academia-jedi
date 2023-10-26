"""Testes dojo20231016."""
# !/usr/bin/env python
import pytest

from incolume.academia_jedi.\
    ajedi20231020_fatorar_romanos_arabicos.dojo import from_roman

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('CD', 400),
        ('XC', 90),
        ('CM', 900),
        ('CMLXXXVII', 987),
        ('MCMLXXVIII', 1978),
        ('I', 1),
        ('II', 2),
        ('III', 3),
        ('IV', 4),
        ('VIII', 8),
        ('IX', 9),
        ('C', 100),
        ('L', 50),
        ('M', 1000),
        ('MCMLXXXVIII', 1988),
        ('MMIX', 2009),
        ('MMXI', 2011),
        ('D', 500),
        ('MD', 1500),
    ],
)
def test_from_roman(entrance, expected) -> None:
    """Testa os resultados entrados e esperando da função from_roman."""
    assert from_roman(entrance) == expected
