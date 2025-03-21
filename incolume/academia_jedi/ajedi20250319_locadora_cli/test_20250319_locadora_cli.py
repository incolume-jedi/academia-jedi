"""Tests Locadora CLI."""

from typing import NoReturn
from unittest import mock

import pytest
from . import Categoria, Montadora, Veiculo, fileconf, config, veiculos
from .asimov import (
    alugados,
    carros,
    devolver_carro,
    place_holder_carros,
    Carro,
    mostrar_lista_carros,
    alugar_carro,
    clear,
)

from dataclasses import is_dataclass


class TestLocadoraAsimov:
    """Testcase."""

    @pytest.mark.parametrize(
        'entrance tipo expected'.split(),
        [
            pytest.param(alugados, list, True, marks=[]),
            pytest.param(carros, list, True, marks=[]),
            pytest.param(place_holder_carros, str, True, marks=[]),
        ],
    )
    def test_0(self, entrance, tipo, expected) -> NoReturn:
        """Unittest."""
        assert isinstance(entrance, tipo) is expected

    def test_1(self) -> NoReturn:
        """Unittest."""
        assert is_dataclass(Carro)

    @pytest.mark.parametrize(
        'entrance attr expected'.split(),
        [
            (carros[4], 'montadora', 'Hyundai'),
            (carros[4], 'modelo', 'HB20S'),
        ],
    )
    def test_2(self, entrance, attr, expected) -> NoReturn:
        """Unittest."""
        assert getattr(entrance, attr) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                carros,
                '[0] Tracker (Chevrolet) - R$ 120 /dia.\n'
                '[1] Onix (Chevrolet) - R$ 90 /dia.\n'
                '[2] Spin (Chevrolet) - R$ 150 /dia.\n'
                '[3] HB20 (Hyundai) - R$ 85 /dia.\n'
                '[4] HB20S (Hyundai) - R$ 110 /dia.\n'
                '[5] Tucson (Hyundai) - R$ 120 /dia.\n'
                '[6] Uno (Fiat) - R$ 60 /dia.\n'
                '[7] Mobi (Fiat) - R$ 70 /dia.\n'
                '[8] Pulse (Fiat) - R$ 130 /dia.\n\n',
            ),
        ],
    )
    def test_mostrar_lista_carros(
        self,
        capsys,
        entrance,
        expected,
    ) -> NoReturn:
        """Unittest."""
        mostrar_lista_carros(ls_carros=entrance)
        capture = capsys.readouterr()
        assert capture.out == expected

    @pytest.mark.parametrize(
        'entrance side_effect expected'.split(),
        [
            pytest.param(
                {
                    'ls_carros': [Carro('Gurgel', 'Xavante XT', 1972, 30.5)],
                    'ls_alugados': [],
                },
                ['0', '10', 's'],
                '[0] Xavante XT (Gurgel) - R$ 30.5 /dia.\n\n'
                '==========\n'
                'Você escolheu Gurgel/Xavante XT por 10 dias.\n'
                'Valor total da reserva R$ 305.00\n\n'
                'Parabéns você alugou o Gurgel/Xavante XT(1972)'
                ' por 10 dias, no valor de R$ 305.00.\n',
            ),
            pytest.param(
                {
                    'ls_carros': [Carro('Gurgel', 'Xavante XT', 1972, 30.5)],
                    'ls_alugados': [],
                },
                ['0', '10', 'n'],
                '[0] Xavante XT (Gurgel) - R$ 30.5 /dia.\n\n'
                '==========\n'
                'Você escolheu Gurgel/Xavante XT por 10 dias.\n'
                'Valor total da reserva R$ 305.00\n\n'
                'Reserva cancelada!\n',
            ),
            pytest.param(
                {
                    'ls_carros': [
                        Carro('Gurgel', 'Xavante XT', 1972, 30.5),
                        Carro('Gurgel', 'BR-800', 1995, 17.5),
                    ],
                    'ls_alugados': [],
                },
                [2, 2, '1', '1', 's'],
                '[0] Xavante XT (Gurgel) - R$ 30.5 /dia.\n'
                '[1] BR-800 (Gurgel) - R$ 17.5 /dia.\n\n'
                '==========\n'
                'Você escolheu Gurgel/BR-800 por 1 dias.\n'
                'Valor total da reserva R$ 17.50\n\n'
                'Parabéns você alugou o Gurgel/BR-800(1995)'
                ' por 1 dias, no valor de R$ 17.50.\n',
            ),
        ],
    )
    def test_alugar_carro(
        self,
        capsys,
        entrance,
        side_effect,
        expected,
    ) -> NoReturn:
        """Unittest."""
        with mock.patch(
            'builtins.input',
            side_effect=side_effect,
        ):
            alugar_carro(**entrance)
            capture = capsys.readouterr()
            assert capture.out == expected

    @pytest.mark.parametrize(
        'entrance side_effect expected'.split(),
        [
            (
                {
                    'ls_carros': [
                        Carro('Gurgel', 'BR-800', 1995, 17.5),
                    ],
                    'ls_alugados': [],
                },
                [],
                'Não constam veiculos para devolução.\n',
            ),
            (
                {
                    'ls_carros': [],
                    'ls_alugados': [
                        Carro('Gurgel', 'BR-800', 1995, 17.5),
                    ],
                },
                ['9', '0', 's'],
                'Segue a listagem dos veiculos para devolução.\n'
                '[0] BR-800 (Gurgel) - R$ 17.5 /dia.\n\n'
                'Gurgel/BR-800(1995) Devolvido com sucesso!\n',
            ),
        ],
    )
    def test_devolver_carro(
        self,
        capsys,
        entrance,
        side_effect,
        expected,
    ) -> NoReturn:
        """Unittest."""
        with mock.patch(
            'builtins.input',
            side_effect=side_effect,
        ):
            devolver_carro(**entrance)
            capture = capsys.readouterr()
            assert capture.out == expected
            assert len(entrance['ls_carros'])

    @pytest.mark.parametrize(
        'entrance',
        [
            'os.system',
        ],
    )
    def test_clear(self, entrance) -> NoReturn:
        """Unittest."""
        with mock.patch(entrance) as m:
            clear()
            assert m.called


class TestLocadoraIncolume:
    """Test case."""

    def test_fileconfig(self):
        """Unittest."""
        assert fileconf.is_file()

    def test_variables(self):
        """Unittest."""
        assert isinstance(config, dict)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (Categoria, False),
            (Montadora, False),
            (Veiculo, True),
        ],
    )
    def test_is_dataclass(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert is_dataclass(entrance) is expected

    @pytest.mark.parametrize(
        'entrance fx expected'.split(),
        [
            pytest.param(1, Categoria, 'Carga', marks=[]),
            pytest.param('carga', Categoria, 'Carga', marks=[]),
            pytest.param('Carga', Categoria, 'Carga', marks=[]),
            pytest.param('CARGA', Categoria, 'Carga', marks=[]),
            pytest.param(0, Montadora, 'Indefinida', marks=[]),
            pytest.param('indefinida', Montadora, 'Indefinida', marks=[]),
            pytest.param('Indefinida', Montadora, 'Indefinida', marks=[]),
            pytest.param('INDEFINIDA', Montadora, 'Indefinida', marks=[]),
        ],
    )
    def test_is_enum(self, entrance, fx, expected) -> NoReturn:
        """Unittest."""
        assert fx(entrance).name == expected

    @pytest.mark.parametrize(
        'fenum entrance expected'.split(),
        [
            pytest.param(Categoria, 1, Categoria.Carga, marks=[]),
            pytest.param(Categoria, 2, Categoria.Passeio, marks=[]),
            pytest.param(Categoria, 3, Categoria.Transporte, marks=[]),
            pytest.param(Montadora, 0, Montadora.Indefinida, marks=[]),
            pytest.param(Montadora, 2, Montadora.Byd, marks=[]),
            pytest.param(Montadora, 8, Montadora.Gm, marks=[]),
            pytest.param(
                Montadora,
                'Lada',
                {
                    'expected_exception': ValueError,
                    'match': "'Lada' is not a valid Montadora",
                },
                marks=[],
            ),
        ],
    )
    def test_enum_values(self, fenum, entrance, expected) -> NoReturn:
        """Unittest."""
        if isinstance(expected, dict):
            with pytest.raises(**expected):
                fenum(entrance)
        else:
            assert fenum(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(Categoria, 'Passeio', marks=[]),
            pytest.param(Categoria, 'Carga', marks=[]),
            pytest.param(Categoria, 'Transporte', marks=[]),
            pytest.param(Montadora, 'Indefinida', marks=[]),
            pytest.param(Montadora, 'Fiat', marks=[]),
            pytest.param(Montadora, 'Toyota', marks=[]),
            pytest.param(Montadora, 'Hyundai', marks=[]),
        ],
    )
    def test_enum_names(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert expected in list(entrance.__members__)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'montadora': 'Gurgel',
                    'modelo': 'BR-800',
                    'ano': 1995,
                    'diaria': 17.5,
                    'categoria': 'carga',
                    'chassi': 'XPTO123',
                },
                {
                    'modelo': 'BR-800',
                    'ano': 1995,
                    'montadora': 9,
                    'categoria': 1,
                    'diaria': 17.5,
                    'chassi': 'XPTO123',
                },
            ),
            (
                {
                    'montadora': 'Gurgel',
                    'modelo': 'Xavante XT',
                    'ano': 1972,
                    'diaria': 22.5,
                    'categoria': 'transporte',
                    'chassi': 'XPTO1234',
                },
                {
                    'modelo': 'Xavante XT',
                    'ano': 1972,
                    'montadora': 9,
                    'categoria': 3,
                    'diaria': 22.5,
                    'chassi': 'XPTO1234',
                },
            ),
        ],
    )
    def test_veiculo_class(self, entrance, expected):
        """Unittest."""
        assert Veiculo(**entrance).to_dict() == expected

    def test_loaded_veiculos(self):
        """Unittest."""
        assert all(isinstance(v, Veiculo) for v in veiculos)
