"""Estudos sobre dynaconf."""

# ruff: noqa: S108 SIM112
import os
from typing import NoReturn
import pytest
from incolume.academia_jedi.ajedi20220924_dynaconf.config import settings
from tempfile import gettempdir
from platform import platform
from pathlib import Path

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseDynaconf:
    """Test case dynaconf."""

    @pytest.fixture(autouse=True)
    def _activate_envvar(self) -> None:
        """Configura variáveis de ambiente através do python."""
        os.environ['INCOLUME_MODE'] = 'development'
        os.environ['INCOLUME_AUTHOR'] = 'Ricardo Brito do Nascimento'
        os.environ['INCOLUME_NAME'] = 'MyApp'
        os.environ['INCOLUME_NUM'] = '42'
        os.environ['INCOLUME_FLOAT'] = '4.2'
        os.environ['INCOLUME_BOOL'] = 'true'
        os.environ['INCOLUME_DICT'] = '{foo="bar"}'
        os.environ['INCOLUME_DICT__fuz'] = 'foo'
        os.environ['INCOLUME_NUMBER'] = '@float 42'
        os.environ['INCOLUME_NUMB'] = '@str 42'
        os.environ['INCOLUME_TEMP'] = Path(
            gettempdir(),
            self.__class__.__name__,
        ).as_posix()
        os.environ['INCOLUME_PATH'] = '@format {this.temp}/xpto/{this.NAME}'
        os.environ['INCOLUME_DATA'] = '@json {"key": "value"}'
        os.environ['INCOLUME_DATA__newkey'] = 'new value'

    def test_environ(self):
        """Unittest."""
        assert 'INCOLUME_MODE' in os.environ
        assert os.environ['INCOLUME_MODE'] == 'development'

    def test_envvar(self) -> None:
        """Test envvar."""
        assert os.getenv('INCOLUME_AUTHOR') == 'Ricardo Brito do Nascimento'

    def test_check_mode(self) -> NoReturn:
        """Check dynaconf mode."""
        assert os.environ.get('INCOLUME_MODE')

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

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'msg',
                'Hello World',
                marks=[],
            ),
            pytest.param('name', 'MyApp'),
            pytest.param('num', 42),
            pytest.param('float', 4.2),
            pytest.param('dict', {'foo': 'bar', 'fuz': 'foo'}),
            pytest.param('bool', True),
            pytest.param('author', 'Ricardo Brito do Nascimento'),
            pytest.param('NUMBER', 42.0),
            pytest.param('NUMB', '42'),
            pytest.param(
                'temp',
                '/tmp/TestCaseDynaconf',
                marks=[
                    pytest.mark.skipif(
                        platform().startswith('win'),
                        reason='This is test only for Unix-like.',
                    ),
                ],
            ),
            pytest.param(
                'temp',
                Path(
                    gettempdir(),
                    'TestCaseDynaconf',
                ).as_posix(),
            ),
            pytest.param(
                'PATH',
                Path(
                    gettempdir(),
                    'TestCaseDynaconf',
                    'xpto',
                    'MyApp',
                ).as_posix(),
            ),
            pytest.param('DATA', {'newkey': 'new value', 'key': 'value'}),
            pytest.param('DATA__newkey', 'new value'),
        ],
    )
    def test_env_default(self, entrance, expected) -> None:
        """Test this."""
        assert getattr(settings.from_env('default'), entrance) == expected

    def test_env_production(self) -> None:
        """Test this."""
        assert settings.from_env('production').msg == 'Hello User'

    def test_env_testing(self) -> None:
        """Test this."""
        assert settings.from_env('testing').msg == 'Hello Tester'


# export INCOLUME_APPLICATION=MyApp; python main.py; unset INCOLUME_APPLICATION
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
