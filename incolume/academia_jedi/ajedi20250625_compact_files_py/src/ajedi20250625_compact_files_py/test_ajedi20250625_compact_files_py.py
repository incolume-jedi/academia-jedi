"""Test module."""

from __future__ import annotations
import shutil
from typing import NoReturn, ClassVar
import pytest
from . import compress_file
from pathlib import Path
from tempfile import tempdir
from inspect import stack
from icecream import ic


class TestCompressFile:
    """Test class for compress_file function."""

    BASE: ClassVar = Path(__file__).parents[-6] / 'data_files'
    PATH: ClassVar = None

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.PATH = Path(tempdir, cls.__name__)

        cls.PATH.joinpath(stack()[0][3]).mkdir(
            parents=True,
            exist_ok=True,
        )
        ic(cls.PATH)

    @classmethod
    def teardown_class(cls):
        """Teardown class.

        Teardown da classe. Remove todos os arquivos
         e diretórios gerados ao final.
        """
        shutil.rmtree(cls.PATH / 'xpto', ignore_errors=True)

    def test_compress_file(self) -> NoReturn:
        """Test compress_file function."""
        input_file: Path = self.PATH / 'test_input.txt'
        output_file: Path = self.PATH / 'test_output.gz'

        # Create a sample input file
        input_file.write_text('This is a test file.')

        # Call the compress_file function
        result = compress_file(input_file, output_file)

        # Check if the output file was created
        assert result is True, 'Compression failed'
        assert output_file.exists(), 'Output file does not exist'

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                {
                    'input_file': BASE / 'csv/01Spotify.csv',
                    'output_file': Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_output.gz',
                    ),
                },
                True,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                {
                    'input_file': 'csv/01Spotify.csv',
                    'output_file': Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_output_3.gz',
                    ),
                },
                False,
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_compress(self, entrance, expected) -> NoReturn:
        """Test compress_file function."""
        entrance['output_file'].parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        result = compress_file(**entrance)
        assert result == expected, (
            f'Expected {expected}, got {result} for {entrance}'
        )
