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
    """Testar exercicio01."""
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
    """Testar exercicio02."""
    assert pkg.exercicio02(entrada) == esperado


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        pytest.param('X', 'Sexo Inválido'),
        pytest.param('F', 'F - Feminino'),
        pytest.param('f', 'F - Feminino'),
        pytest.param('M', 'M - Masculino'),
        pytest.param('m', 'M - Masculino'),
        pytest.param('G', 'Sexo Inválido'),
        pytest.param(12, 'Sexo Inválido'),
        pytest.param(False, 'Sexo Inválido'),
    ],
)
def test_exercicio03(entrada, esperado):
    """Testar exercicio03."""
    assert pkg.exercicio03(entrada) == esperado


@pytest.mark.parametrize(
    'entrada esperado'.split(),
    [
        pytest.param('a', 'Vogal'),
        pytest.param('e', 'Vogal'),
        pytest.param('i', 'Vogal'),
        pytest.param('o', 'Vogal'),
        pytest.param('u', 'Vogal'),
        pytest.param('A', 'Vogal'),
        pytest.param('E', 'Vogal'),
        pytest.param('I', 'Vogal'),
        pytest.param('O', 'Vogal'),
        pytest.param('U', 'Vogal'),
        pytest.param('X', 'Consoante'),
        pytest.param('x', 'Consoante'),
        pytest.param('J', 'Consoante'),
        pytest.param('G', 'Consoante'),
    ],
)
def test_exercicio04(entrada, esperado):
    """Testar exercicio04."""
    assert pkg.exercicio04(entrada) == esperado


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 10), 'Aprovado com Distinção'),
        ((7, 7), 'Aprovado'),
        ((7, 9), 'Aprovado'),
        ((7, 6), 'Reprovado'),
    ],
)
def test_exercicio05(entrance, expected):
    """Testar exercicio05."""
    assert pkg.exercicio05(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 9, 1), 10),
        ((10, 100, 1), 100),
        ((9, 21, 1), 21),
        ((9, 21, 1, 3, 6, 7, 9, 13, 0, -12), 21),
    ],
)
def test_exercicio06(entrance, expected):
    """Testar exercicio06."""
    assert pkg.exercicio06(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 9, 1), (10, 1)),
        ((10, 100, 1), (100, 1)),
        ((9, 21, 1), (21, 1)),
        ((9, 21, 1, 3, 6, 7, 9, 13, 0, -12), (21, -12)),
    ],
)
def test_exercicio07(entrance, expected):
    """Testar exercicio07."""
    assert pkg.exercicio07(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 9, 1), 1),
        ((10, 100, 1), 1),
        ((9, 21, 1), 1),
        (
            (
                9,
                21,
                3,
                6,
                7,
                9,
                13,
            ),
            3,
        ),
    ],
)
def test_exercicio08(entrance, expected):
    """Testar exercicio08."""
    assert pkg.exercicio08(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 9, 1), [10, 9, 1]),
        ((10, 100, 1), [100, 10, 1]),
        ((9, 21, 1), [21, 9, 1]),
        (
            (
                9,
                21,
                3,
                6,
                7,
                44,
                13,
            ),
            [44, 21, 13, 9, 7, 6, 3],
        ),
    ],
)
def test_exercicio9(entrance, expected):
    """Testar exercicio9."""
    assert pkg.exercicio9(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('m', 'Bom Dia!'),
        ('M', 'Bom Dia!'),
        ('matutino', 'Bom Dia!'),
        ('Matutino', 'Bom Dia!'),
        ('MATUTINO', 'Bom Dia!'),
        ('v', 'Boa Tarde!'),
        ('V', 'Boa Tarde!'),
        ('vespertino', 'Boa Tarde!'),
        ('Vespertino', 'Boa Tarde!'),
        ('VESPERTINO', 'Boa Tarde!'),
        ('n', 'Boa Noite!'),
        ('N', 'Boa Noite!'),
        ('noturno', 'Boa Noite!'),
        ('Noturno', 'Boa Noite!'),
        ('NOTURNO', 'Boa Noite!'),
    ],
)
def test_exercicio10(entrance, expected):
    """Testar exercicio10."""
    assert pkg.exercicio10(entrance) == expected


@pytest.mark.parametrize(
    'entrance excpt'.split(),
    [
        (
            'Guitarra',
            {
                'expected_exception': ValueError,
                'match': 'Turno inválido: "Guitarra".',
            },
        ),
        (
            'G',
            {
                'expected_exception': ValueError,
                'match': 'Turno inválido: "G".',
            },
        ),
    ],
)
def test_exercicio10_exceptions(entrance, excpt):
    """Testar exercicio10."""
    with pytest.raises(**excpt):
        pkg.exercicio10(entrance)


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            1500.01,
            'Salário atual: R$  1500.01\n aumento: 5.0 %\n aumento: R$  75.00\n Salário novo: R$ 1575.01',
        ),
        (
            280,
            'Salário atual: R$  280.00\n aumento: 20.0 %\n aumento: R$  56.00\n Salário novo: R$ 336.00',
        ),
        (
            700,
            'Salário atual: R$  700.00\n aumento: 15.0 %\n aumento: R$  105.00\n Salário novo: R$ 805.00',
        ),
        (
            1500,
            'Salário atual: R$  1500.00\n aumento: 10.0 %\n aumento: R$  150.00\n Salário novo: R$ 1650.00',
        ),
    ],
)
def test_exercicio11(entrance, expected):
    """Testar exercicio11."""
    assert pkg.exercicio11(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, '1-Domingo'),
        (2, '2-Segunda'),
        (3, '3-Terça'),
        (4, '4-Quarta'),
        (5, '5-Quinta'),
        (6, '6-Sexta'),
        (7, '7-Sabado'),
        (8, 'valor inválido'),
        ('a', 'valor inválido'),
        (8.0, 'valor inválido'),
    ],
)
def test_exercicio13(entrance, expected):
    """Testar exercicio13."""
    assert pkg.exercicio13(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 10), 'A'),
        ((7, 7), 'C'),
        ((7, 9), 'B'),
        ((7, 6), 'C'),
        ((5, 5), 'D'),
        ((0, 2), 'E'),
    ],
)
def test_exercicio14(entrance, expected):
    """Testar exercicio14."""
    assert pkg.exercicio14(*entrance) == expected