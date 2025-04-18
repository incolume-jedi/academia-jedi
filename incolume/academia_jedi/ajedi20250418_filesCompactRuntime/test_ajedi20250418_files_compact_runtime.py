"""Estudo sobre compactação em runtime."""

import io
from typing import NoReturn
import zipfile

import pytest
import incolume.academia_jedi.ajedi20250418_filesCompactRuntime as pkg
from pathlib import Path
from tempfile import gettempdir
from icecream import ic
from config import settings
import httpx


ic.disable()
if settings.debug_mode:
    ic.enable()


class TestCase:
    """TestCase."""

    target_file: str = 'source/dignissimos.txt'

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.localzip = pkg.set_env(count=15, seed=191)

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
            b'\xc2\xb9\xe2\x81\xb6 Porque Deus amou o mundo de'
            b' tal maneira que deu o seu '
            b'Filho unig\xc3\xaanito,\n',
            b' para que todo aquele que nele cr\xc3\xaa n\xc3\xa3o'
            b' pere\xc3\xa7a, mas te'
            b'nha a vida eterna.\n',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open('source/dignissimos.txt') as file,
        ):
            assert ic(expected).issubset(ic(file.readlines()))

    def test_3(self) -> NoReturn:
        """Unittest."""
        expected = {
            '¹⁶ Porque Deus amou o mundo de tal maneira que deu o'
            ' seu Filho unigênito,\n',
            ' para que todo aquele que nele crê não pereça,'
            ' mas tenha a vida eterna.\n',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open(self.target_file) as file,
        ):
            result = [line.decode('utf-8') for line in file]
            assert expected.issubset(result)

    def test_4(self) -> NoReturn:
        """Unittest."""
        file_zip = io.BytesIO(httpx.get(pkg.URL.zip).content)
        target_file = 'CLEAN_FIFA23_official_data.csv'
        expected = (
                b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                b'Preferred Foot,International Reputation,Weak Foot,Skill'
                b' Moves,Work Rate,Body Type,Real Face,Position,Joined,'
                b'Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.)'
                b',Release Clause(\xc2\xa3),Kit Number,Best Overall Rating,'
                b'Year_Joined\r\n'
            )

        with (
            zipfile.ZipFile(file_zip) as handle,
            handle.open(target_file) as file,
        ):
            assert file.readline() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA17_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA17_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA18_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA18_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA19_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA19_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA20_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA20_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA21_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA21_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA22_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA22_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA23_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA23_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason='Dont found the input files')],
            ),
        ],
    )
    def test_5(self, entrance, expected) -> NoReturn:
        """Unittest."""
        file_zip = self.localzip.parent / f'{entrance.stem}.zip'
        assert pkg.gen_zip(members=[entrance], zipname=file_zip) == expected

    def test_6(self) -> NoReturn:
        """Unittest."""
        entrance = (
            Path.home()
            .joinpath('Downloads', 'archive')
            .glob('CLEAN_FIFA*_official_data.csv')
        )
        expected = Path(gettempdir()).joinpath(
            'ajedi20250418_filesCompactRuntime',
            'CLEAN_FIFA.zip',
        )
        file_zip = self.localzip.parent / 'CLEAN_FIFA.zip'
        assert (
            pkg.gen_zip(members=ic(list(entrance)), zipname=file_zip)
            == expected
        )
