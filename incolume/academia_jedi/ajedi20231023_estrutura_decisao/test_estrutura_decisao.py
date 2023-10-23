"""Testes unitários para estrutura de decisão."""
import incolume.academia_jedi.ajedi20231023_estrutura_decisao.estrutura_decisao as pkg
import pytest


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        ((1, 2), 2),
        ((5, 2), 5),
        ((4, 4), 4),
    ],
)
def test_exercicio01(entrada, esperado):
    """testar exercicio01."""
    assert pkg.exercicio01(*entrada) == esperado


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        pytest.param(0, 'neutro', marks=''),
        (-1, 'negativo'),
        (1, 'positivo'),
    ],
)
def test_exercicio02(entrada, esperado):
    """testar exercicio02."""
    assert pkg.exercicio02(entrada) == esperado


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        pytest.param("X", "Sexo Inválido"),
        pytest.param("F", "F - Feminino"),
        pytest.param("f", "F - Feminino"),
        pytest.param("M", "M - Masculino"),
        pytest.param("m", "M - Masculino"),
        pytest.param("G", "Sexo Inválido"),
        pytest.param(12, "Sexo Inválido"),
        pytest.param(False, "Sexo Inválido"),
    ],
)
def test_exercicio03(entrada, esperado):
    """testar exercicio03."""
    assert pkg.exercicio03(entrada) == esperado


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        pytest.param("a", "Vogal"),
        pytest.param("e", "Vogal"),
        pytest.param("i", "Vogal"),
        pytest.param("o", "Vogal"),
        pytest.param("u", "Vogal"),
        pytest.param("A", "Vogal"),
        pytest.param("E", "Vogal"),
        pytest.param("I", "Vogal"),
        pytest.param("O", "Vogal"),
        pytest.param("U", "Vogal"),
        pytest.param("X", "Consoante"),
        pytest.param("x", "Consoante"),
        pytest.param("J", "Consoante"),
        pytest.param("G", "Consoante"),
    ],
)
def test_exercicio04(entrada, esperado):
    """testar exercicio04."""