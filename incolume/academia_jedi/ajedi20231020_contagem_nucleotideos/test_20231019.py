"""Teste dojo contagem de nucleotídeos."""

import pytest

from incolume.academia_jedi.ajedi20231020_contagem_nucleotideos.dojo import (
    contador_nucleotideos, 
    cont_nucleotideos,
)


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('ATCG', '1 1 1 1'),
        ('ATATGGCC', '2 2 2 2'),
        ('ATGCTTCAGAAAGGTCTTACG', '6 4 5 6'),
        (
            'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT'
            'CTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC',
            '20 12 16 20',
        ),
        ('AAAAACCCCGGGTT', '5 4 3 2'),
    ],
)
def test_contador_nucleotideos(entrance, expected) -> None:
    """Testar a função contador_nucleotideos."""
    assert contador_nucleotideos(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('ATCG', '1 1 1 1'),
        ('ATATGGCC', '2 2 2 2'),
        ('ATGCTTCAGAAAGGTCTTACG', '6 4 5 6'),
        (
            'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT'
            'CTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC',
            '20 12 16 20',
        ),
        ('AAAAACCCCGGGTT', '5 4 3 2'),
    ],
)
def test_contador_nucleotideos(entrance, expected) -> None:
    """Testar a função contador_nucleotideos."""
    assert cont_nucleotideos(entrance) == expected