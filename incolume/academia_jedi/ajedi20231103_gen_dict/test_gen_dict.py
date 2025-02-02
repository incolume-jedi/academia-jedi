import pytest

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import logging
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa01 import d
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa02 import (
    get_client_google,
    set_credentials,
)
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa03 import GSheet
from tempfile import NamedTemporaryFile
from pathlib import Path
import re
import json


__author__ = '@britodfbr'  # pragma: no cover


class TestCaseTratativa01:
    """Test case."""

    def test_dict(self):
        """Test d."""
        assert isinstance(d, dict)


class TestCaseTratativa02:
    """Test case."""

    @pytest.fixture()
    def fakefile(self) -> Path:
        """Fake file."""
        return Path(NamedTemporaryFile(prefix='academia-jedi-').name)

    @pytest.mark.skip(reason='ValueError: Invalid format string')
    def test_set_credentials_0(self, caplog, fakefile) -> None:
        """Test this."""
        json.dump({}, fakefile.open('w'))
        with caplog.at_level(level=logging.DEBUG):
            result: Path = set_credentials(fakefile)
            assert result == fakefile

    @pytest.mark.skip(reason='ValueError: Invalid format string')
    def test_set_credentials_1(self, caplog, fakefile) -> None:
        """Test this."""
        with caplog.at_level(level=logging.DEBUG):
            fakefile.write_text('{}')
            set_credentials(fakefile)
            assert (
                f'return: {fakefile.as_posix()}' in caplog.records[-1].message
            )

    @pytest.mark.skip(reason='ValueError: Invalid format string')
    def test_set_credentials_2(self, caplog) -> None:
        """Test this."""
        with caplog.at_level(level=logging.DEBUG):
            set_credentials()
            assert re.fullmatch(
                r'return: .*/private/authkeys/.*',
                caplog.records[-1].message,
            )

    @pytest.mark.skip()
    def test_set_credentials(self) -> None:
        """Test this."""
        with pytest.raises(FileExistsError, match=''):
            set_credentials()

    @pytest.mark.skip()
    def test_get_client_google(self, fakefile) -> None:
        """Test this."""
        fakefile.write_text('')
        assert get_client_google(fakefile)

    # def test_get_url_sheet(self) -> None:
    #     """Test this."""
    #     assert get_url_sheet() == ''

    # def test_load_sheet(self) -> None:
    #     """Test this."""
    #     assert load_create_sheet()

    # def test_drop_sheet(self) -> None:
    #     """Test this."""
    #     assert drop_sheet('')


class TestCaseTratativa03:
    @pytest.fixture()
    def obj_gsheet(self):
        """Objeto GSheet."""
        return GSheet()

    def test_1(self) -> None:
        """Test credential file."""
        # cred = Path('//castelo/saj').joinpath(,'EQUIPE CEJ','BRITO','projetos','private','authkeys','incolumepy-dev-6ae65605985c.json')
        cred = Path(r'H:\CENTRO DE ESTUDOS\EQUIPE CEJ\BRITO')
        assert cred.is_dir()

    @pytest.mark.skip(reason='FileNotFoundError')
    def test_0(self, obj_gsheet):
        """Test 1."""
        obj_gsheet.escopo == ''
