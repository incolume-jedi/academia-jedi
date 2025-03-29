"""Test module."""

import inspect
from pathlib import Path
import shutil
from tempfile import gettempdir
from typing import NoReturn
import requests
import pytest
from incolume.academia_jedi.ajedi20221220_web_scraping_bs4 import (
    my_scrap_imdb,
    my_scrap_imdb1,
    my_scrap_imdb2,
)
from platform import platform


class TestCase:
    """TestCase."""

    output_dir: Path = Path(gettempdir()) / f'{inspect.stack()[0][3]}'

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.output_dir.mkdir(exist_ok=True, parents=True)

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        shutil.rmtree(cls.output_dir, ignore_errors=True)

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(raises=requests.exceptions.ReadTimeout)
    def test_0(self) -> NoReturn:
        """Unittest."""
        fileoutput = self.output_dir / f'{inspect.stack()[0][3]}.xlsx'
        my_scrap_imdb.scraping_ranking(excel_output=fileoutput)
        assert fileoutput.is_file()

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_1(self) -> NoReturn:
        """Unittest."""
        fileoutput = self.output_dir / f'{inspect.stack()[0][3]}.xlsx'
        my_scrap_imdb1.scraping_ranking1(excel_output=fileoutput)
        assert fileoutput.is_file()

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_2(self) -> NoReturn:
        """Unittest."""
        fileoutput = self.output_dir / f'{inspect.stack()[0][3]}.xlsx'
        scrap_imdb = my_scrap_imdb2.ScrapingIMDB()
        scrap_imdb.connect().get_soup().get_movies().save_excel(
            excel_output=fileoutput,
        )
        assert fileoutput.is_file()

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_3(self) -> NoReturn:
        """Unittest."""
        fileoutput = self.output_dir / f'{inspect.stack()[0][3]}.xlsx'
        my_scrap_imdb2.ScrapingIMDB().scraping(excel_output=fileoutput)
        assert fileoutput.is_file()

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_4(self) -> NoReturn:
        """Unittest."""
        assert my_scrap_imdb.scraping_ranking(
            excel_output=Path(gettempdir()) / 'abc.xlsx',
        )

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_5(self) -> NoReturn:
        """Unittest."""
        assert my_scrap_imdb1.scraping_ranking1(
            excel_output=Path(gettempdir()) / 'bcd.xlsx',
        )

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_6(self) -> NoReturn:
        """Unittest."""
        assert my_scrap_imdb2.ScrapingIMDB().scraping(excel_output='a1b2.xlsx')

    @pytest.mark.skipif(condition=platform().casefold()[:3]=='win',reason='Does not run on MS-Windows.')
    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason='Timeout connection',
    )
    def test_7(self) -> NoReturn:
        """Unittest."""

    scrap_imdb = my_scrap_imdb2.ScrapingIMDB()
    scrap_imdb.connect().get_soup().get_movies().save_excel(
        excel_output=Path(gettempdir()) / 'xpto.xlsx',
    )
