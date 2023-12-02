"""Test Jokenpo."""
from copy import copy

from faker import Faker
import pytest
from incolume.academia_jedi.ajedi20231201_jokenpo import main
from secrets import choice

__author__ = "@britodfbr"  # pragma: no cover
fake = Faker('pt-BR')


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'PAPEL'),
        (2, 'TESOURA'),
        (3, 'PEDRA'),
    ]
)
def test_enum(entrance, expected) -> None:
    """Test enum."""
    assert main.Jokenpo(entrance) == getattr(main.Jokenpo, expected)


def jogador(nome: str = '', lance: main.Jokenpo | None = None):
    nome = nome or fake.name()
    lance = lance or main.Jokenpo(choice(range(1, 4)))
    return main.Jogador(nome=nome, lance=lance)


def test_jogador_assinatura() -> None:
    """Test enum."""
    assert jogador().__annotations__ == {
        'derrotas': int, 'empates': int,
        'vitorias': int,
        'lance': main.Jokenpo,
        'nome': str,
    }


@pytest.mark.parametrize(
    'entrance1 entrance2 expected'.split(),
    [
        (
            jogador(lance=main.Jokenpo(1)),
            jogador(lance=main.Jokenpo(1)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(1)),
            jogador(lance=main.Jokenpo(2)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(1)),
            jogador(lance=main.Jokenpo(3)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(2)),
            jogador(lance=main.Jokenpo(1)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(2)),
            jogador(lance=main.Jokenpo(2)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(2)),
            jogador(lance=main.Jokenpo(3)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(3)),
            jogador(lance=main.Jokenpo(1)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(3)),
            jogador(lance=main.Jokenpo(2)),
            False
        ),
        (
            jogador(lance=main.Jokenpo(3)),
            jogador(lance=main.Jokenpo(3)),
            False
        ),
    ]
)
def test_jogador_op_relacionais(entrance1, entrance2, expected) -> None:
    """Test enum."""
    assert (entrance1 > entrance2) == expected
