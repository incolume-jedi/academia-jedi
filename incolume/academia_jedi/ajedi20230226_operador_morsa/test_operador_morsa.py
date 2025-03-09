"""Test module."""

from typing import NoReturn

import pytest
import incolume.academia_jedi.ajedi20230226_operador_morsa.exemplo1 as ex1


# ruff: noqa: ERA001 FIX002


class TestOpMorsa:
    """Test class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'func': ex1.menu},
                'Escolha um numero (zero (0) para sair): ',
                marks=[
                    pytest.mark.skip(
                        reason='#TODO(britodfbr): correção, '
                        'pois a saida deve mostrar menu',
                    ),
                ],
            ),
            pytest.param(
                {'func': ex1.menu},
                '',
                marks=[],
            ),
            pytest.param(
                {'func': ex1.run},
                '',
                marks=[],
            ),
        ],
    )
    def test_exemplo1_menu(
        self,
        entrance,
        expected,
        capsys,
        monkeypatch,
    ) -> NoReturn:
        """Unittest."""
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: '0')
            assert isinstance(entrance, dict)
            entrance['func']()
            out, err = capsys.readouterr()
            assert out == expected
            assert err == ''
