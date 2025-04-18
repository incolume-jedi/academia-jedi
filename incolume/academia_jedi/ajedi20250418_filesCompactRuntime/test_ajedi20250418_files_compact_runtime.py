"""Estudo sobre compactação em runtime."""

import io
from typing import NoReturn
import zipfile
import incolume.academia_jedi.ajedi20250418_filesCompactRuntime as pkg
from pathlib import Path
from tempfile import gettempdir
from icecream import ic
from config import settings


ic.disable()
if settings.debug_mode:
    ic.enable()


class TestCase:
    """TestCase."""
    target_file: str ='source/dignissimos.txt'

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.localzip = pkg.set_env()

    @classmethod
    def teardown_class(cls):
        """Teardown class."""

    def test_0(self) -> NoReturn:
        """Unittest."""
        assert self.localzip == Path(gettempdir()).joinpath(
            'ajedi20250418_filesCompactRuntime',
            'archives.zip',
        )

    def test_1(self) -> NoReturn:
        """Unittest."""
        expected = (
            'Porque Deus amou o mundo de tal maneira que deu o seu Filho'
            ' unigênito,\n para que todo aquele que nele crê não pereça,'
            ' mas tenha a vida eterna.'
        )
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open(self.target_file) as file,
        ):
            assert expected in io.TextIOWrapper(file, encoding='utf-8').read()

    def test_2(self) -> NoReturn:
        """Unittest."""
        expected = {
            b'\xc2\xb9\xe2\x81\xb6 Porque Deus amou o mundo de tal maneira que deu o seu '
            b'Filho unig\xc3\xaanito,',
            b' para que todo aquele que nele cr\xc3\xaa n\xc3\xa3o pere\xc3\xa7a, mas te'
            b'nha a vida eterna.',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open('source/dignissimos.txt') as file,
        ):
            # assert expected == file.readlines()
            assert ic(expected).issubset(ic(file.readlines()))

    def test_3(self) -> NoReturn:
        """Unittest."""
        expected = {
            '¹⁶ Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito,\n',
            ' para que todo aquele que nele crê não pereça, mas tenha a vida eterna.\n',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open(self.target_file) as file,
        ):
            result = [line.decode('utf-8') for line in file]
            assert set(result) == set(expected)
            # assert expected in result
            assert expected.issubset(result)
