"""Module oracle."""

from __future__ import annotations
from pathlib import Path
import incolume.academia_jedi.ajedi20250504_oraculo_ai as pkg
from incolume.academia_jedi.ajedi20250504_oraculo_ai.utils import (
    midia_loader,
    load_web,
    load_yt,
)
from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    YoutubeLoader,
)
import pytest
from icecream import ic


class TestAjedi20250504OraculoAI:
    """Test class for Ajedi20250504OraculoAI."""

    path: Path = Path(__file__).parents[3] / 'data_files'

    def test_path(self):
        """Test the path."""
        assert self.path.exists()

    def test_ajedi20250504_oraculo_ai_module(self):
        """Test the oracle AI module."""
        assert (
            pkg.__name__ == 'incolume.academia_jedi.ajedi20250504_oraculo_ai'
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'https://www4.planalto.gov.br/centrodeestudos/',
                'Centro de Estudos Jurídicos',
            ),
            pytest.param(
                'https://asimov.academy/',
                'Asimov. Todos os direitos reservado.'
                ' CNPJ: 41.075.192/0001-82',
            ),
            pytest.param(
                'https://www4.planalto.gov.br/centrodeestudos/perguntas-frequentes/',
                'Confira aqui as perguntas mais frequentes enviadas ao'
                ' Centro de Estudos. Alguma delas pode'
                ' responder suas questões.',
            ),
        ],
    )
    def test_web_loader(self, entrance, expected):
        """Test the web loader."""
        content = load_web(entrance)
        ic(content)
        assert len(content) > 0
        assert expected in content

    def test_youtube_loader(self):
        """Test the youtube loader."""
        entrance = 'IGDaXFmb1NU'
        expected = 'Doclin'
        content = load_yt(video_id=entrance)
        ic(content)
        assert len(content) > 0
        assert expected in content

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'midia': path.joinpath(
                        'csv',
                        'aniversariantes.csv',
                    ),
                    'loader': CSVLoader,
                },
                '',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {
                    'midia': path.joinpath('pdf', 'Ilustrator.pdf'),
                    'loader': PyPDFLoader,
                },
                '',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {
                    'midia': path.joinpath(
                        'csv',
                        'aniversariantes.csv',
                    ).as_posix(),
                    'loader': TextLoader,
                },
                '',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {
                    'midia': 'https://www4.planalto.gov.br/centrodeestudos/',
                    'loader': WebBaseLoader,
                },
                '',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {'midia': 'IGDaXFmb1NU', 'loader': YoutubeLoader},
                '',
                marks=[pytest.mark.skip],
            ),
        ],
    )
    def test_utils(self, entrance, expected):
        """Test the oracle AI module."""
        assert midia_loader(**entrance) == expected
