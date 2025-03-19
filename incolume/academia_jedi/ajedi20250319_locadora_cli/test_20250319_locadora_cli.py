"""Tests Locadora CLI."""

from enum import IntEnum
from typing import NoReturn

import pytest
from . import Categoria, Montadora, Veiculo, fileconf, config
from dataclasses import is_dataclass


class TestLocadora:
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
            pytest.param(Categoria, 1, Categoria.passeio, marks=[]),
            pytest.param(Categoria, 2, Categoria.carga, marks=[]),
            pytest.param(Categoria, 3, Categoria.transporte, marks=[]),
            pytest.param(Montadora, 1, Montadora.indefinida, marks=[]),
            pytest.param(Montadora, 2, Montadora.byd, marks=[]),
            pytest.param(Montadora, 3, Montadora.gm, marks=[]),
        ],
    )
    def test_enum_values(self, fenum, entrance, expected) -> NoReturn:
        """Unittest."""
        assert fenum(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                Categoria,
                Categoria.passeio,
                marks=[],
            ),
            pytest.param(Montadora, Montadora.indefinida, marks=[]),
        ],
    )
    def test_enum_names(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert expected in list(entrance.__members__.values)

    def test_0(self):
        """Unittest."""
        assert Montadora.__members__ == {}
        # assert Montadora.__members__.items() == []
