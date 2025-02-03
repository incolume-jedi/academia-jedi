"""Others tests."""

import io
from pathlib import Path
from unittest import mock
from icecream import ic
from tempfile import gettempdir
import os

__author__ = '@britodfbr'  # pragma: no cover


class UnixFS:
    """Class UnixFS."""

    @staticmethod
    def rm(filename: Path) -> bool:
        """Function rm."""
        filename = Path(filename)
        os.remove(filename)  # noqa: PTH107
        return not filename.exists()


def test_unix_fs():
    """Exemplo pytest-mock."""
    file = Path(gettempdir()) / 'file.txt'
    file.write_text('..')
    with mock.patch('os.remove') as mkos:
        UnixFS.rm(file)
        mkos.assert_called_once_with(file)


def test_method(monkeypatch):
    """Test method."""
    monkeypatch.setattr('sys.stdin', io.StringIO('+'))


def ask(idade_min: int = 12) -> None:
    """For test bad params."""
    while (idade := int(input('informe a tua idade: '))) < idade_min:
        if idade < idade_min:
            ic(f'You are too young({idade})')
    nome = input('informe o teu nome: ')
    ic(f'Welcome! {nome.capitalize()}({idade})')


@mock.patch('builtins.input', side_effect=['11', '13', 'Bob'])
def test_ask(capsys):
    """Unittest."""
    ask()
    output = capsys.readouterr()
    # Check the output after "13" and "Bob" are entered as well!
    assert output.out == 'You are too young(11)\nWelcome! Bob(13)\n'


def test_bad_params(capsys):
    """Test for bad params."""
    with mock.patch('builtins.input', side_effect=['15', '11', '19', 'Bet']):
        ask(18)
        output = capsys.readouterr()
        assert output.out == (
            'You are too young(15)\nYou are too young(11)\nWelcome! Bet(19)\n'
        )
