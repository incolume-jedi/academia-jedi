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