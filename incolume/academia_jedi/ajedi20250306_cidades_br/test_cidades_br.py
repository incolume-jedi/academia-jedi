"""Test module."""

from pathlib import Path
from typing import ClassVar, Final, NoReturn

import pytest
import incolume.academia_jedi.ajedi20250306_cidades_br as pkg
import tempfile


# ruff: noqa: SLF001
class TestMunicipios0:
    """TestMunicipios class."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(pkg.mg, list, marks=[]),
            pytest.param(pkg.sp, list, marks=[]),
            pytest.param(pkg.cidades_file_txt, Path, marks=[]),
        ],
    )
    def test_variables(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert isinstance(entrance, expected)

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('exists', True),
            pytest.param('is_file', True),
            pytest.param('is_dir', False, marks=[]),
        ],
    )
    def test_cidades_file(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert getattr(pkg.cidades_file_txt, entrance)() == expected

    def test_length_get_cities_sp_645(self) -> NoReturn:
        """Unittest."""
        total: Final[int] = 645
        assert len(pkg.get_cities_sp()) == total

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param('Adamantina', marks=[]),
            pytest.param('Adolfo', marks=[]),
            pytest.param('Águas da Prata', marks=[]),
            pytest.param('Águas de Lindóia', marks=[]),
            pytest.param('Águas de Santa Bárbara', marks=[]),
            pytest.param('Águas de São Pedro', marks=[]),
            pytest.param('Votuporanga', marks=[]),
            pytest.param('Zacarias', marks=[]),
        ],
    )
    def test_get_cities_sp(self, entrance) -> NoReturn:
        """Unittest."""
        assert {entrance}.issubset(pkg.get_cities_sp())


class TestMunicipios:
    """TestMunicipios class."""

    records: ClassVar[tuple[int, int]] = (5570, 4)

    def test_get_cities_type(self) -> NoReturn:
        """Unittest."""
        assert isinstance(
            pkg._get_cities_dataframe_from_csv(),
            pkg.pd.DataFrame,
        )

    def test_get_cities_shape(self) -> NoReturn:
        """Unittest."""
        assert pkg._get_cities_dataframe_from_csv().shape == self.records

    def test_get_cities_length(self) -> NoReturn:
        """Unittest."""
        assert len(pkg._get_cities_dataframe_from_csv()) == self.records[0]

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param('Adamantina', marks=[]),
            pytest.param('Adolfo', marks=[]),
            pytest.param('Águas da Prata', marks=[]),
            pytest.param('Águas de Lindóia', marks=[]),
            pytest.param('Águas de Santa Bárbara', marks=[]),
            pytest.param('Águas de São Pedro', marks=[]),
            pytest.param('Votuporanga', marks=[]),
            pytest.param('Zacarias', marks=[]),
        ],
    )
    def test_get_cities_name(self, entrance) -> NoReturn:
        """Unittest."""
        assert {entrance}.issubset(pkg.get_cities())

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            ('', 'output.yaml'),
            (None, 'output.yaml'),
            (
                Path(tempfile.gettempdir()) / 'municípios_br.yaml',
                'municípios_br.yaml',
            ),
        ],
    )
    def test_pandas2yaml(self, entrance, expected) -> NoReturn:
        """Unitest."""
        data = {
            'dataframe': pkg._get_cities_dataframe_from_csv()[
                ['municipio', 'uf']
            ],
            'filename': entrance,
        }
        assert expected in pkg.pandas2yaml(**data).as_posix()
