"""Testes unitários para estrutura de decisão."""
import io

import mock
import pytest

import incolume.academia_jedi.ajedi20231023_estrutura_decisao.estrutura_decisao as pkg


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
    """Testar exercicio09."""
    assert pkg.exercicio09(*entrance) == expected


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
            'Salário atual: R$  1500.01\n aumento: 5.0 %\n'
            ' aumento: R$  75.00\n Salário novo: R$ 1575.01',
        ),
        (
            280,
            'Salário atual: R$  280.00\n aumento: 20.0 %\n'
            ' aumento: R$  56.00\n Salário novo: R$ 336.00',
        ),
        (
            700,
            'Salário atual: R$  700.00\n aumento: 15.0 %\n'
            ' aumento: R$  105.00\n Salário novo: R$ 805.00',
        ),
        (
            1500,
            'Salário atual: R$  1500.00\n aumento: 10.0 %\n'
            ' aumento: R$  150.00\n Salário novo: R$ 1650.00',
        ),
    ],
)
def test_exercicio11(entrance, expected):
    """Testar exercicio11."""
    assert pkg.exercicio11(entrance) == expected


def test_exercicio12(capsys):
    """Testar exercicio 12."""
    pkg.exercicio12(5, 220)
    out, err = capsys.readouterr()
    assert out == (
        '\n            Salário Bruto: (5 * 220): R$ 1100'
        '\n            (-) IR (5%)                     : R$   0'
        '\n            (-) INSS ( 10%)                 : R$  110.0'
        '\n            FGTS (11%)                      : R$  121.0'
        '\n            Total de descontos              : R$  121.0'
        '\n            Salário Liquido                 : R$  979.0'
        '\n'
    )


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
        ((10, 10), 'Notas: (10.0, 10.0), Média: 10.0, Conceito: A "APROVADO"'),
        ((7, 7), 'Notas: (7.0, 7.0), Média: 7.0, Conceito: C "APROVADO"'),
        ((7, 9), 'Notas: (7.0, 9.0), Média: 8.0, Conceito: B "APROVADO"'),
        ((7, 6), 'Notas: (7.0, 6.0), Média: 6.5, Conceito: C "APROVADO"'),
        ((5, 5), 'Notas: (5.0, 5.0), Média: 5.0, Conceito: D "REPROVADO"'),
        ((0, 2), 'Notas: (0.0, 2.0), Média: 1.0, Conceito: E "REPROVADO"'),
        (
            (10, 9, 0, 2),
            'Notas: (10.0, 9.0, 0.0, 2.0), Média: 5.25, Conceito: D "REPROVADO"',
        ),
    ],
)
def test_exercicio14(entrance, expected):
    """Testar exercicio14."""
    assert pkg.exercicio14(*entrance) == expected


@pytest.mark.parametrize(
    'entrance xcpt'.split(),
    [
        (
            (10, 'a'),
            {
                'expected_exception': ValueError,
                'match': 'Somente valores numéricos',
            },
        ),
        (
            ('A', 7),
            {
                'expected_exception': ValueError,
                'match': 'Somente valores numéricos',
            },
        ),
        (
            ('a', '9'),
            {
                'expected_exception': ValueError,
                'match': 'Somente valores numéricos',
            },
        ),
        (
            ('', 6),
            {
                'expected_exception': ValueError,
                'match': 'Somente valores numéricos',
            },
        ),
    ],
)
def test_exercicio14_exceptions(entrance, xcpt):
    """Testar exercicio14."""
    with pytest.raises(**xcpt):
        pkg.exercicio14(*entrance)


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((2, 3, 5), 'Triângulo escaleno'),
        ((1, 1, 1), 'Triângulo equilátero'),
        ((8, 9, 8), 'Triângulo isósceles'),
        ((4, 4, 4), 'Triângulo equilátero'),
    ],
)
def test_exercicio15(entrance, expected) -> None:
    """Testar exercicio15."""
    assert pkg.exercicio15(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (2000, True),
        (2020, True),
        (2021, False),
        (2022, False),
        (2023, False),
        (2024, True),
    ],
)
def test_exercicio17(entrance, expected) -> None:
    """Testar exercicio 17."""
    assert pkg.exercicio17(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('1/1/2001', True),
        ('5/11/2023', True),
        ('35/11/2000', False),
        ('29/2/2000', True),
        ('29/2/2020', True),
        ('29/2/2021', False),
        ('29/2/2022', False),
        ('29/2/2023', False),
    ],
)
def test_exercicio18(entrance, expected) -> None:
    """Testar exercicio 18."""
    assert pkg.exercicio18(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (326, '3 centenas 2 dezenas 6 unidades'),
        (12, '1 dezena 2 unidades'),
        (300, '3 centenas 0 dezena 0 unidade'),
        (100, '1 centena 0 dezena 0 unidade'),
        (320, '3 centenas 2 dezenas 0 unidade'),
        (310, '3 centenas 1 dezena 0 unidade'),
        (305, '3 centenas 0 dezena 5 unidades'),
        (301, '3 centenas 0 dezena 1 unidade'),
        (101, '1 centena 0 dezena 1 unidade'),
        (311, '3 centenas 1 dezena 1 unidade'),
        (111, '1 centena 1 dezena 1 unidade'),
        (25, '2 dezenas 5 unidades'),
        (20, '2 dezenas 0 unidade'),
        (10, '1 dezena 0 unidade'),
        (21, '2 dezenas 1 unidade'),
        (11, '1 dezena 1 unidade'),
        (1, '1 unidade'),
        (7, '7 unidades'),
        (16, '1 dezena 6 unidades'),
    ],
)
def test_exercicio19(entrance, expected):
    """Testar exercicio19."""
    assert pkg.exercicio19(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((0, 0, 0), '0.0 - Reprovado'),
        ((5, 6, 8), '6.3 - Reprovado'),
        ((7, 7, 7), '7.0 - Aprovado'),
        ((10, 10, 10), '10.0 - Aprovado com Distinção'),
    ],
)
def test_exercicio20(entrance, expected):
    """Teste do exercício20."""
    assert pkg.exercicio20(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'impar'),
        (10, 'par'),
        (13, 'impar'),
        (100, 'par'),
    ],
)
def test_exercicio22(entrance, expected):
    """Testar exercicio22."""
    assert pkg.exercicio22(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'inteiro'),
        (1.0, 'inteiro'),
        (3.1415, 'decimal'),
        (100, 'inteiro'),
    ],
)
def test_exercicio23(entrance, expected):
    """Testar exercicio23."""
    assert pkg.exercicio23(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (('+', 1, 2), '3.00 impar positivo inteiro'),
        (('/', 7, 3), '2.33 par positivo decimal'),
        (('*', 1, 3.1415), '3.14 impar positivo decimal'),
        (('-', 1, 2), '-1.00 impar negativo inteiro'),
    ],
)
def test_exercicio24(entrance, expected):
    """Testar exercicio24."""
    with mock.patch('builtins.input', side_effect=entrance):
        assert pkg.exercicio24() == expected
