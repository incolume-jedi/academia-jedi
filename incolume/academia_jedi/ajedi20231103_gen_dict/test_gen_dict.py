import pytest
import logging
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa01 import d
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa02 import drop_sheet, load_create_sheet, get_client_google, get_url_sheet, set_credentials
from incolume.academia_jedi.ajedi20231103_gen_dict.tratativa03 import GSheet
from tempfile import NamedTemporaryFile
from pathlib import Path
import re


__author__ = '@britodfbr'  # pragma: no cover


class TestCaseTratativa01:
    """Test case."""
    def test_dict(self):
        """Test d."""
        assert isinstance(d, dict)


class TestCaseTratativa02:
    """Test case."""

    def test_set_credentials_0(self, caplog) -> None:
        """Test this."""
        fakefile = Path(NamedTemporaryFile(prefix='ajedi-').name)
        fakefile.write_text("{}")
        with caplog.at_level(level=logging.DEBUG):
            result = set_credentials(fakefile)
            assert result == fakefile

    def test_set_credentials_1(self, caplog) -> None:
        """Test this."""
        fakefile = Path(NamedTemporaryFile(prefix='ajedi-').name)
        with caplog.at_level(level=logging.DEBUG):
            fakefile.write_text("{}")
            set_credentials(fakefile)
            assert (f'return: {fakefile.as_posix()}'
                    in caplog.records[-1].message)

    def test_set_credentials_2(self, caplog) -> None:
        """Test this."""
        with caplog.at_level(level=logging.DEBUG):
            set_credentials()
            assert re.fullmatch(
                r'return: .*/private/authkeys/.*',
                caplog.records[-1].message
            )

    @pytest.mark.skip
    def test_set_credentials(self, fakefile) -> None:
        """Test this."""
        assert set_credentials().as_posix() == ''

    def test_get_client_google(self, fakefile) -> None:
        """Test this."""
        fakefile.write_text('')
        assert get_client_google(fakefile)

    def test_get_url_sheet(self) -> None:
        """Test this."""
        assert get_url_sheet() == ''

    def test_load_sheet(self) -> None:
        """Test this."""
        assert load_create_sheet()

    def test_drop_sheet(self) -> None:
        """Test this."""
        assert drop_sheet('')



class TestCaseTratativa03:
    @pytest.fixture()
    def obj_gsheet():
        """Objeto GSheet."""
        return GSheet()
    
    def test_0(self, obj_gsheet):
        """Test 1."""
        obj_gsheet.escopo == ''

