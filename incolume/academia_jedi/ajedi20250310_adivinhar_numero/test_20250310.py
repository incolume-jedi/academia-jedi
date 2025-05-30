"""Test module."""

import pytest
import incolume.academia_jedi.ajedi20250310_adivinhar_numero as pkg
from icecream import ic
from config import settings

ic.disable()
if settings['DEBUG_MODE']:
    ic.enable()

ic.disable()


@pytest.mark.parametrize(
    ['num', 'entrance', 'expected'],
    [
        pytest.param(0, 0, 'parabéns você acertou!!!\n'),
        pytest.param(
            1,
            0,
            'O número é maior que o palpite\n',
        ),
        pytest.param(
            0,
            1,
            'O número é menor que o palpite\n',
        ),
    ],
)
def test_jogo(monkeypatch, capsys, num, entrance, expected):
    """Unittest."""
    with monkeypatch.context() as m:
        m.setattr('secrets.randbelow', lambda _: num)
        m.setattr('builtins.input', lambda _: entrance)
        pkg.jogo(tries=1)
        out, err = capsys.readouterr()
        assert out == expected
        assert err == ''
