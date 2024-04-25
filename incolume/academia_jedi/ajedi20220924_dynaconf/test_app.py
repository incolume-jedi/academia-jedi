# !/usr/bin/env python
from os import environ, getenv
from typing import NoReturn
from unittest import mock
import pytest

from incolume.academia_jedi.ajedi20220924_dynaconf.config import settings

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseDynaconf:
    """Test case dynaconf."""

    @pytest.fixture(autouse=True)
    def activate_envvar(self) -> None:
        """Configura variáveis de ambiente através do python."""
        environ['INCOLUME_MODE'] = 'development'
        environ['INCOLUME_AUTHOR'] = 'Ricardo Brito do Nascimento'
        environ['INCOLUME_NAME'] = 'MyApp'
        environ['INCOLUME_NUM'] = '42'
        environ['INCOLUME_FLOAT'] = '4.2'
        environ['INCOLUME_BOOL'] = 'true'
        environ['INCOLUME_DICT'] = '{foo="bar", fuz="foo"}'
        environ['INCOLUME_NUMBER'] = '@float 42'
        environ['INCOLUME_NUMB'] = '@str 42'
        environ['INCOLUME_PATH'] = '@format /tmp/xpto/{this.NAME}'
        environ['INCOLUME_DATA'] = '@json {"key": "value"}'
        environ['INCOLUME_DATA__newkey'] = 'new value'

    def test_envvar(self) -> None:
        """Test envvar."""
        assert getenv('INCOLUME_AUTHOR') == 'Ricardo Brito do Nascimento'

    def test_check_mode(self) -> NoReturn:
        """Check dynaconf mode."""
        assert environ.get('INCOLUME_MODE')

    @pytest.mark.parametrize(
        'entrance',
        [
            settings.MSG,
            settings.msg,
            settings.get('MSG'),
            settings.get('msg'),
            settings['MSG'],
            settings['msg'],
        ],
    )
    def test_development_msg(self, entrance) -> None:
        """Test msg default."""
        assert entrance == 'Hello Dev'

    @pytest.mark.skip(reason='Need mock environment variable mode.')
    def test_default_msg(self) -> None:
        """Test this."""
        with mock.patch.dict(environ, {'INCOLUME_MODE': 'default'}):
            # environ['INCOLUME_MODE'] = 'default'
            assert settings.msg == 'Hello World'

    @pytest.mark.skip(reason='Need mock environment variable mode.')
    def test_production_msg(self) -> None:
        """Test this."""
        environ['INCOLUME_MODE'] = 'production'
        assert settings.msg == 'Hello User'

    @pytest.mark.skip(reason='Need mock environment variable mode.')
    def test_testing_msg(self) -> None:
        """Test this."""
        environ['INCOLUME_MODE'] = 'testing'
        assert settings.msg == 'Hello Tester'


#  export INCOLUME_APPLICATION=MyApp; python main.py; unset INCOLUME_APPLICATION
"""
$ export INCOLUME_NUM=42
$ export INCOLUME_FLOAT=4.2
$ export INCOLUME_DICT='{foo="bar"}'
$ export INCOLUME_BOOL=false
$ export INCOLUME_NAME=MyApp
$ dynaconf --instance config.settings list
    Working in main environment
    MSG<str> 'Hello World'
    NUM<int> 42
    NAME<str> 'MyApp'
    DICT<dict> {'foo': 'bar'}
    FLOAT<float> 4.2
    BOOL<bool> False
export INCOLUME_MODE='production'; dynaconf --instance config.settings list
export INCOLUME_MODE='testing'; dynaconf --instance config.settings list
export INCOLUME_MODE='development'; dynaconf --instance config.settings list

"""
