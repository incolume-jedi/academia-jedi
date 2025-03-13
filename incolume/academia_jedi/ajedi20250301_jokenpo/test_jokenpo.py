"""Test Jokenpo."""

from __future__ import annotations
import sys
from faker import Faker
import pytest
from incolume.academia_jedi import ajedi20250301_jokenpo
from secrets import choice


__author__ = '@britodfbr'  # pragma: no cover

Faker.seed(13)
fake = Faker('pt-BR')


def jogador(
    nome: str = '',
    lance: ajedi20250301_jokenpo.Jokenpo | None = None,
) -> ajedi20250301_jokenpo.Jogador:
    """Definir jogador.

    Args:
        nome (str, optional): _description_. Defaults to ''.
        lance (main.Jokenpo | None, optional): _description_. Defaults to None.

    Returns:
        None: Nonetype
    """
    nome = nome or fake.name()
    lance = lance or ajedi20250301_jokenpo.Jokenpo(choice(range(1, 4)))
    return ajedi20250301_jokenpo.Jogador(nome=nome, lance=lance)


class TestJokenpo:
    """Test Case."""

    j1 = jogador(lance=ajedi20250301_jokenpo.Jokenpo('papel'))
    j2 = jogador(lance=ajedi20250301_jokenpo.Jokenpo('papel'))

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, 'PAPEL'),
            (2, 'TESOURA'),
            (3, 'PEDRA'),
            ('papel', 'PAPEL'),
            ('tesoura', 'TESOURA'),
            ('pedra', 'PEDRA'),
        ],
    )
    def test_enum(self, entrance, expected) -> None:
        """Test enum."""
        assert ajedi20250301_jokenpo.Jokenpo(entrance) == getattr(
            ajedi20250301_jokenpo.Jokenpo,
            expected,
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('PAPEL', 1),
            ('TESOURA', 2),
            ('PEDRA', 3),
            (1, 1),
            (2, 2),
            (3, 3),
        ],
    )
    def test_enum_rev(self, entrance, expected) -> None:
        """Test enum."""
        assert ajedi20250301_jokenpo.Jokenpo(
            entrance,
        ) == ajedi20250301_jokenpo.Jokenpo(expected)

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                ajedi20250301_jokenpo.Jogador,
                marks=[
                    pytest.mark.skipif(
                        sys.version_info < (3, 13),
                        reason=r"This test don't run on python"
                        ' below 3.13 version.',
                    ),
                ],
            ),
            pytest.param(
                ajedi20250301_jokenpo.Jogador(
                    'John Doe',
                    ajedi20250301_jokenpo.Jokenpo('pedra'),
                ),
                marks=[
                    pytest.mark.skipif(
                        sys.version_info < (3, 13),
                        reason=r"This test don't run on python"
                        ' below 3.13 version.',
                    ),
                ],
            ),
            pytest.param(
                jogador(),
                marks=[
                    pytest.mark.skipif(
                        sys.version_info < (3, 13),
                        reason=r"This test don't run on python"
                        ' below 3.13 version.',
                    ),
                ],
            ),
        ],
    )
    def test_jogador_assinatura(self, entrance) -> None:
        """Test enum."""
        assert entrance.__annotations__['derrotas'] == 'int'
        assert entrance.__annotations__['empates'] == 'int'
        assert entrance.__annotations__['vitorias'] == 'int'
        assert entrance.__annotations__['lance'] == 'Jokenpo'
        assert entrance.__annotations__['nome'] == 'str'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('papel', 1), True),
            pytest.param(('papel', 'papel'), True),
            pytest.param(('papel', 'PAPEL'), True),
            pytest.param(('papel', 2), False),
            pytest.param(('papel', 'tesoura'), False),
            pytest.param(('papel', 'TESOURA'), False),
            pytest.param(('papel', 3), False),
            pytest.param(('papel', 'pedra'), False),
            pytest.param(('papel', 'PEDRA'), False),
            pytest.param(('tesoura', 3), False),
            pytest.param(('tesoura', 'pedra'), False),
            pytest.param(('tesoura', 'PEDRA'), False),
        ],
    )
    def test_jokenpo_equals(self, entrance, expected):
        """Unittest."""
        value1, value2 = entrance
        result = ajedi20250301_jokenpo.Jokenpo(
            value1,
        ) == ajedi20250301_jokenpo.Jokenpo(value2)
        assert result == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('papel', 1), False),
            pytest.param(('papel', 'papel'), False),
            pytest.param(('papel', 'PAPEL'), False),
            pytest.param(('papel', 2), True),
            pytest.param(('papel', 'tesoura'), True),
            pytest.param(('papel', 'TESOURA'), True),
            pytest.param(('papel', 3), False),
            pytest.param(('papel', 'pedra'), False),
            pytest.param(('papel', 'PEDRA'), False),
            pytest.param(('tesoura', 1), False),
            pytest.param(('tesoura', 'papel'), False),
            pytest.param(('tesoura', 'PAPEL'), False),
            pytest.param(('tesoura', 2), False),
            pytest.param(('tesoura', 'tesoura'), False),
            pytest.param(('tesoura', 'TESOURA'), False),
            pytest.param(('tesoura', 3), True),
            pytest.param(('tesoura', 'pedra'), True),
            pytest.param(('tesoura', 'PEDRA'), True),
            pytest.param(('pedra', 1), True),
            pytest.param(('pedra', 'papel'), True),
            pytest.param(('pedra', 'PAPEL'), True),
            pytest.param(('pedra', 2), False),
            pytest.param(('pedra', 'tesoura'), False),
            pytest.param(('pedra', 'TESOURA'), False),
            pytest.param(('pedra', 3), False),
            pytest.param(('pedra', 'pedra'), False),
            pytest.param(('pedra', 'PEDRA'), False),
        ],
    )
    def test_jokenpo_less_than(self, entrance, expected):
        """Unittest."""
        value1, value2 = entrance
        result = ajedi20250301_jokenpo.Jokenpo(
            value1,
        ) < ajedi20250301_jokenpo.Jokenpo(value2)
        assert result == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('papel', 1), False),
            pytest.param(('papel', 'papel'), False),
            pytest.param(('papel', 'PAPEL'), False),
            pytest.param(('papel', 2), False),
            pytest.param(('papel', 'tesoura'), False),
            pytest.param(('papel', 'TESOURA'), False),
            pytest.param(('papel', 3), True),
            pytest.param(('papel', 'pedra'), True),
            pytest.param(('papel', 'PEDRA'), True),
            pytest.param(('tesoura', 1), True),
            pytest.param(('tesoura', 'papel'), True),
            pytest.param(('tesoura', 'PAPEL'), True),
            pytest.param(('tesoura', 2), False),
            pytest.param(('tesoura', 'tesoura'), False),
            pytest.param(('tesoura', 'TESOURA'), False),
            pytest.param(('tesoura', 3), False),
            pytest.param(('tesoura', 'pedra'), False),
            pytest.param(('tesoura', 'PEDRA'), False),
            pytest.param(('pedra', 1), False),
            pytest.param(('pedra', 'papel'), False),
            pytest.param(('pedra', 'PAPEL'), False),
            pytest.param(('pedra', 2), True),
            pytest.param(('pedra', 'tesoura'), True),
            pytest.param(('pedra', 'TESOURA'), True),
            pytest.param(('pedra', 3), False),
            pytest.param(('pedra', 'pedra'), False),
            pytest.param(('pedra', 'PEDRA'), False),
        ],
    )
    def test_jokenpo_greater_than(self, entrance, expected):
        """Unittest."""
        value1, value2 = entrance
        result = ajedi20250301_jokenpo.Jokenpo(
            value1,
        ) > ajedi20250301_jokenpo.Jokenpo(value2)
        assert result == expected

    @pytest.mark.parametrize(
        'entrance1 entrance2 expected'.split(),
        [
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(1)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(1)),
                'Breno Teixeira X Vinicius Gonçalves: Empate.',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(1)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                'Leandro Costela X Maria Alves: Maria Alves Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(1)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(3)),
                'Danilo Cardoso X Levi Pinto: Danilo Cardoso Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(1)),
                'Fernando Moraes X Luigi Vieira: Fernando Moraes Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                'Lara Moreira X Maysa Lopes: Empate.',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(3)),
                'Ana Vitória Monteiro X Yasmin Ferreira:'
                ' Yasmin Ferreira Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo('pedra')),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo('papel')),
                'Sra. Maria Clara Cunha X Nicole Pires:'
                ' Nicole Pires Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(3)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(2)),
                'Camila Gonçalves X Davi Silveira: Camila Gonçalves Ganhou!!!',
                marks=[],
            ),
            pytest.param(
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(3)),
                jogador(lance=ajedi20250301_jokenpo.Jokenpo(3)),
                'Dr. João Lucas Ramos X Otávio Freitas: Empate.',
                marks=[],
            ),
        ],
    )
    def test_jogador_op_relacionais(
        self,
        entrance1,
        entrance2,
        expected,
    ) -> None:
        """Test enum."""
        assert (
            ajedi20250301_jokenpo.start_jokenpo(entrance1, entrance2)
            == expected
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'papel',
                "Jogador(nome='Gustavo da Mata',"
                ' vitorias=0, derrotas=0, empates=1)',
                marks=[],
            ),
            pytest.param(
                'papel',
                "Jogador(nome='Gustavo da Mata',"
                ' vitorias=0, derrotas=0, empates=2)',
                marks=[],
            ),
            pytest.param(
                'tesoura',
                "Jogador(nome='Gustavo da Mata',"
                ' vitorias=1, derrotas=0, empates=2)',
                marks=[],
            ),
            pytest.param(
                'pedra',
                "Jogador(nome='Gustavo da Mata',"
                ' vitorias=1, derrotas=1, empates=2)',
                marks=[],
            ),
        ],
    )
    def test_placar(self, entrance, expected):
        """Test resultados."""
        self.j1.lance = ajedi20250301_jokenpo.Jokenpo(entrance)
        ajedi20250301_jokenpo.start_jokenpo(self.j1, self.j2)
        assert str(self.j1) == expected
