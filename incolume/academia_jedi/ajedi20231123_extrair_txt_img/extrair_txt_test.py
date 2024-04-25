"""Unittest."""

from pathlib import Path

import pytest

import incolume.academia_jedi.ajedi20231107_extrair_txt_pdf.tratativa01 as pkg

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseTratativa01:
    """Testcase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'img2.png'),
                'RICARDO',
            ),
            (
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'img3.png'),
                'Acai',
            ),
            pytest.param(
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'myimage.png'),
                '',
                marks=pytest.mark.skip(reason='Cursivo não identificável.'),
            ),
        ],
    )
    def test_exemplo01(self, entrance, expected) -> None:
        """Teste exemplo01."""
        assert pkg.exemplo01(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'img2.png'),
                'RICARDO',
            ),
            (
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'img3.png'),
                'Açaí',
            ),
            pytest.param(
                Path(__file__)
                .parents[3]
                .joinpath('data_files', 'img', 'myimage.png'),
                '',
                marks=pytest.mark.skip(reason='Cursivo não identificável.'),
            ),
        ],
    )
    def test_exemplo02(self, entrance, expected) -> None:
        """Teste exemplo02."""
        assert pkg.exemplo02(entrance) == expected

    def test_exemplo03(self) -> None:
        """Teste exemplo03."""
