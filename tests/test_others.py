"""Others tests."""

import io
import os
from unittest import mock
import sys

__author__ = '@britodfbr'  # pragma: no cover


class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    """Exemplo pytest-mock."""
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')


def test_method(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('+'))


def ask(idade_min: int = 12):
    """For test bad params."""
    while (idade := int(input('informe a tua idade: '))) < idade_min:
        if idade < idade_min:
            print(f'You are too young({idade})')
    else:
        nome = input('informe o teu nome: ')
        print(f'Welcome! {nome.capitalize()}({idade})')


@mock.patch('builtins.input', side_effect=['11', '13', 'Bob'])
def test_ask(input, capsys):
    ask()
    out, err = capsys.readouterr()
    # Check the output after "13" and "Bob" are entered as well!
    assert out == 'You are too young(11)\nWelcome! Bob(13)\n'


def test_bad_params(capsys):
    with mock.patch('builtins.input', side_effect=['15', '11', '19', 'Bet']):
        ask(18)
        out, err = capsys.readouterr()
        assert out == (
            'You are too young(15)\nYou are too young(11)\nWelcome! Bet(19)\n'
        )
