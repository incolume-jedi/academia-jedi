import pytest

from incolume.academia_jedi.ajedi20231020_massa_test_codons.codons import (
    massa_codon_dna,
    massa_codon_dna0,
    massa_codon_dna1,
)


@pytest.mark.parametrize(
    'entrance',
    [
        5,
        12,
        999,
        1000,
        3,
        2,
        1,
        0,
        1004,
        80000,
        99779,
    ],
)
def test_massa_codon_dna_alfabeto0(entrance: int) -> None:
    """Testar alfabeto contido no codon."""
    alfabeto: str = 'ATGC'
    assert all(s in alfabeto for s in massa_codon_dna0(entrance))


@pytest.mark.parametrize(
    'entrance',
    [
        5,
        12,
        999,
        1000,
        3,
        2,
        1,
        0,
        1004,
        80000,
        99779,
    ],
)
def test_massa_codon_dna_limites0(entrance: int) -> None:
    """Testar limites maximos e minimos de caracteres."""
    assert len(massa_codon_dna0(entrance)) >= 4
    assert len(massa_codon_dna0(entrance)) <= 1000


@pytest.mark.skip()
@pytest.mark.parametrize(
    'entrance',
    [
        5,
        12,
        999,
        1000,
        3,
        2,
        1,
        0,
        1004,
        80000,
        99779,
    ],
)
def test_massa_codon_dna_alfabeto(entrance: int) -> None:
    """Testar alfabeto contido no codon."""
    alfabeto: str = 'ATGC'
    assert all(s in alfabeto for s in massa_codon_dna(entrance))


@pytest.mark.skip()
@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        (5, True),
        (12, True),
        (999, True),
        (1000, True),
        (3, False),
        (2, False),
        (1, False),
        (0, False),
        (1004, False),
        (80000, False),
        (99779, False),
    ],
)
def test_massa_codon_dna_limites1(entrance: int, expected: bool) -> None:
    """Testar limites maximos e minimos de caracteres."""
    assert (4 <= len(massa_codon_dna1(entrance)) <= 1000) == expected


@pytest.mark.parametrize(
    ('entrance', 'exceptions'),
    [
        (5, None),
        (12, None),
        (999, None),
        (1000, None),
        (
            3,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho inferior ao limite de 4',
            },
        ),
        (
            2,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho inferior ao limite de 4',
            },
        ),
        (
            1,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho inferior ao limite de 4',
            },
        ),
        (
            0,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho inferior ao limite de 4',
            },
        ),
        (
            1004,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho superior ao limite de 1000',
            },
        ),
        (
            80000,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho superior ao limite de 1000',
            },
        ),
        (
            99779,
            {
                'expected_exception': ValueError,
                'match': 'Tamanho superior ao limite de 1000',
            },
        ),
    ],
)
def test_massa_codon_dna_limites(entrance: int, exceptions) -> None:
    """Testar limites maximos e minimos de caracteres."""
    if exceptions:
        with pytest.raises(**exceptions):
            massa_codon_dna(entrance)
    else:
        assert len(massa_codon_dna(entrance)) == entrance
