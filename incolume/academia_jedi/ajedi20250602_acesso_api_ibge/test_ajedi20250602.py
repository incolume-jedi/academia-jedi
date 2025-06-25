"""Test for ajedi20250602_acesso_api_ibge package."""

from __future__ import annotations
import pytest


import incolume.academia_jedi.ajedi20250602_acesso_api_ibge as pkg
from icecream import ic


class TestAjedi20250602AcessoApiIbge:
    """Test class for ajedi20250602_acesso_api_ibge package."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                {'url_api': pkg.url_api.format(nome='ada')},
                [
                    {
                        'localidade': 'BR',
                        'nome': 'ADA',
                        'res': [
                            {'frequencia': 333, 'periodo': '1930['},
                            {'frequencia': 513, 'periodo': '[1930,1940['},
                            {'frequencia': 550, 'periodo': '[1940,1950['},
                            {'frequencia': 623, 'periodo': '[1950,1960['},
                            {'frequencia': 707, 'periodo': '[1960,1970['},
                            {'frequencia': 568, 'periodo': '[1970,1980['},
                            {'frequencia': 739, 'periodo': '[1980,1990['},
                            {'frequencia': 689, 'periodo': '[1990,2000['},
                            {'frequencia': 573, 'periodo': '[2000,2010['},
                        ],
                        'sexo': None,
                    },
                ],
            ),
            pytest.param(
                {'params': {}, 'url_api': pkg.url_api.format(nome='ana')},
                [
                    {
                        'localidade': 'BR',
                        'nome': 'ANA',
                        'res': [
                            {'frequencia': 33395, 'periodo': '1930['},
                            {'frequencia': 56160, 'periodo': '[1930,1940['},
                            {'frequencia': 101259, 'periodo': '[1940,1950['},
                            {'frequencia': 183941, 'periodo': '[1950,1960['},
                            {'frequencia': 292835, 'periodo': '[1960,1970['},
                            {'frequencia': 421531, 'periodo': '[1970,1980['},
                            {'frequencia': 529266, 'periodo': '[1980,1990['},
                            {'frequencia': 536302, 'periodo': '[1990,2000['},
                            {'frequencia': 935169, 'periodo': '[2000,2010['},
                        ],
                        'sexo': None,
                    },
                ],
            ),
        ],
    )
    def test_get_api(self, entrance, expected) -> None:
        """Test get_api function."""
        response = pkg.get_api(**entrance)
        ic(response)
        assert isinstance(response, list)
        assert response == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                {'nome': 'ada'},
                {'frequencia', 'periodo'},
            ),
            pytest.param(
                {'params': {}, 'nome': 'ana'},
                {'frequencia', 'periodo'},
            ),
            pytest.param(
                {'nome': 'ariel', 'params': {'sexo': 'F'}},
                {'frequencia', 'periodo'},
            ),
            pytest.param(
                {'nome': 'ariel', 'params': {'sexo': 'M'}},
                {'frequencia', 'periodo'},
            ),
            pytest.param(
                {'nome': 'ada', 'params': {'sexo': 'F', 'groupBy': 'UF'}},
                {'frequencia', 'populacao', 'proporcao'},
            ),
            pytest.param(
                {'nome': 'ada', 'params': {'sexo': 'M', 'groupBy': 'UF'}},
                {'frequencia', 'populacao', 'proporcao'},
            ),
        ],
    )
    def test_get_nome(self, entrance, expected) -> None:
        """Test get_api function."""
        response = pkg.get_nome(**entrance)
        ic(response)
        assert expected.issubset(response[0]['res'][0].keys())

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                'UF-id',
                42,
            ),
            pytest.param(
                'UF-sigla',
                'DF',
            ),
        ],
    )
    def test_get_region(self, entrance, expected) -> None:
        """Test get_region function."""
        response = pkg.get_region()
        assert all(r for r in response if r.get(entrance) == expected)

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                'UF-id',
                42,
            ),
            pytest.param(
                'UF-sigla',
                'DF',
            ),
        ],
    )
    def test_get_uf(self, entrance, expected) -> None:
        """Test get_uf function."""
        response = pkg.get_uf()
        ic(response)
        assert all(r for r in response if r.get(entrance) == expected)
