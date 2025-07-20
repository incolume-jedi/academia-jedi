"""Test module."""

from __future__ import annotations
import shutil
from typing import NoReturn, ClassVar
import pytest
from . import compress_file, decompress_file
from pathlib import Path
from tempfile import tempdir
from inspect import stack
from icecream import ic
from dataclasses import dataclass, fields


@dataclass
class Entrance:
    """Entrance data class for test parameters."""

    input_file: Path | str
    output_file: Path | str

    def keys(self):
        """Return the names of the fields in the dataclass."""
        return (f.name for f in fields(self))

    def __getitem__(self, item):
        """Return the value of the given attribute name."""
        return getattr(self, item)


class TestCompressFile:
    """Test class for compress_file function."""

    BASE: ClassVar = Path(__file__).parents[-6] / 'data_files'
    PATH: ClassVar = Path(tempdir, stack()[0][3])

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.PATH.joinpath(stack()[0][3]).mkdir(
            parents=True,
            exist_ok=True,
        )
        ic(f'{cls.PATH=}')
        ic(f'{cls.BASE=}')

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
                Entrance(
                    input_file=BASE / 'csv/01Spotify.csv',
                    output_file=Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_output.gz',
                    ),
                ),
                True,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(
                    'csv/01Spotify.csv',
                    Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_output_3.gz',
                    ),
                ),
                False,
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_compress(self, entrance, expected) -> NoReturn:
        """Test compress_file function."""
        result = compress_file(**entrance)
        assert result == expected, (
            f'Expected {expected}, got {result} for {entrance}'
        )

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                Entrance(
                    output_file=PATH / 'csv/01Spotify.csv',
                    input_file=Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_input0.gz',
                    ),
                ),
                True,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(
                    Path(
                        tempdir,
                        stack()[0][3],
                        'xpto',
                        'test_input1.gz',
                    ),
                    PATH / 'c3po' / 'csv' / '01Spotify.csv',
                ),
                True,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(
                    input_file=PATH / 'r2d2' / 'test_output.gz',
                    output_file=PATH / 'r2d2' / 'test_decompressed.txt',
                ),
                True,
                marks=[],
            ),
        ],
    )
    def test_decompress_file(self, entrance, expected) -> NoReturn:
        """Test decompress_file function."""
        # Create a sample compressed file
        compress_file(
            input_file=self.BASE / 'csv/01Spotify.csv',
            output_file=entrance.input_file,
        )

        # Call the decompress_file function
        result = decompress_file(**entrance)

        # Check if the output file was created
        assert result is expected, 'Decompression failed'
        assert entrance.output_file.is_file(), 'Output file does not exist'

    def test_decompress_file_invalid(self) -> NoReturn:
        """Test decompress_file with an invalid file."""
        input_file = self.PATH / 'invalid.gz'
        output_file = self.PATH / 'invalid_output.txt'

        # Call the decompress_file function with an invalid file
        result = decompress_file(input_file, output_file)

        # Check if the result is False
        assert not result, 'Decompression should have failed for invalid file'
        assert not output_file.exists(), 'Output file should not exist'
