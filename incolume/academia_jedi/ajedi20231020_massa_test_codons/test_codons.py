import pytest

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
