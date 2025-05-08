"""Module oracle."""

from __future__ import annotations
from pathlib import Path
import incolume.academia_jedi.ajedi20250504_oraculo_ai as pkg
from incolume.academia_jedi.ajedi20250504_oraculo_ai.utils import (
    midia_loader,
)
from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    YoutubeLoader,
)
import pytest


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
            ),
            pytest.param(
                {'midia': 'IGDaXFmb1NU', 'loader': YoutubeLoader},
                '',
            ),
        ],
    )
    def test_utils(self, entrance, expected):
        """Test the oracle AI module."""
        assert midia_loader(**entrance) == expected
