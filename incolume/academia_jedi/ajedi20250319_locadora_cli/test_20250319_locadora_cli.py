"""Tests Locadora CLI."""

from enum import IntEnum
from typing import NoReturn
from unittest import mock

import pytest
from . import Categoria, Montadora, Veiculo, fileconf, config
from .asimov import (
    alugados,
    carros,
    place_holder_carros,
    Carro,
    mostrar_lista_carros,
    alugar_carro,
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
                ['0', '10'],
                '[0] Xavante XT (Gurgel) - R$ 30.5 /dia.\n\n'
                '==========\n'
                'Você escolheu Gurgel/Xavante XT por 10 dias.\n'
                'Valor total da reserva R$ 305.00\n\n'
                'Parabéns você alugou o Gurgel/Xavante XT(1972)'
                ' por 10 dias, no valor de R$ 305.00.\n',
            ),
            pytest.param(
                {
                    'ls_carros': [
                        Carro('Gurgel', 'Xavante XT', 1972, 30.5),
                        Carro('Gurgel', 'BR-800', 1995, 17.5),
                    ],
                    'ls_alugados': [],
                },
                [2, 2, 1, 1],
                '',
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
        'entrance expected'.split(),
        [
            pytest.param(Categoria, True, marks=[pytest.mark.skip]),
            pytest.param(Montadora, True, marks=[pytest.mark.skip]),
            pytest.param(Veiculo, False, marks=[pytest.mark.skip]),
        ],
    )
    def test_is_enum(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert isinstance(entrance, IntEnum) is expected

    @pytest.mark.parametrize(
        'fenum entrance expected'.split(),
        [
            pytest.param(Categoria, 1, Categoria.carga, marks=[]),
            pytest.param(Categoria, 2, Categoria.passeio, marks=[]),
            pytest.param(Categoria, 3, Categoria.transporte, marks=[]),
            pytest.param(Montadora, 0, Montadora.indefinida, marks=[]),
            pytest.param(Montadora, 2, Montadora.byd, marks=[]),
            pytest.param(Montadora, 8, Montadora.gm, marks=[]),
        ],
    )
    def test_enum_values(self, fenum, entrance, expected) -> NoReturn:
        """Unittest."""
        assert fenum(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(Categoria, 'passeio', marks=[]),
            pytest.param(Categoria, 'carga', marks=[]),
            pytest.param(Categoria, 'transporte', marks=[]),
            pytest.param(Montadora, 'indefinida', marks=[]),
            pytest.param(Montadora, 'fiat', marks=[]),
            pytest.param(Montadora, 'toyota', marks=[]),
            pytest.param(Montadora, 'hyundai', marks=[]),
        ],
    )
    def test_enum_names(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert expected in list(entrance.__members__)

    def test_0(self):
        """Unittest."""
        # assert Montadora.__members__ == {}
