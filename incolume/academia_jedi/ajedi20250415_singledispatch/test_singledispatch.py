"""Test module."""

from __future__ import annotations

import pytest
import incolume.academia_jedi.ajedi20250415_singledispatch as pkg
import cmath

__all__ = ['cmath']


class TestCase:
    """Case de teste para singledispatch."""

    @pytest.mark.parametrize(
        'entrance kwargs expected'.split(),
        [
            pytest.param('', {}, '', marks=[]),
            pytest.param(
                '',
                {'verbose': True},
                ('Let me just say,', ''),
                marks=[],
            ),
            pytest.param('Jesus te ama!', {}, 'Jesus te ama!', marks=[]),
            pytest.param(
                'Tudo é dificil até fácil se tornar.',
                {},
                'Tudo é dificil até fácil se tornar.',
                marks=[],
            ),
            pytest.param(
                'Tudo é dificil até fácil se tornar.',
                {'verbose': True},
                ('Let me just say,', 'Tudo é dificil até fácil se tornar.'),
                marks=[],
            ),
            pytest.param(
                1,
                {'verbose': True},
                ('Strength in numbers, eh?', 1),
                marks=[],
            ),
            pytest.param(
                3.14,
                {'verbose': True},
                ('Strength in numbers, eh?', 3.14),
                marks=[],
            ),
            pytest.param(
                tuple('abc'),
                {'verbose': True},
                ('Enumerate this tuple:', (0, 'a'), (1, 'b'), (2, 'c')),
                marks=[],
            ),
            pytest.param(
                set('abc'),
                {'verbose': True},
                ['Enumerate this set:', (0, 'a'), (1, 'b'), (2, 'c')],
                marks=[
                    # pytest.mark.xfail
                ],
            ),
            pytest.param(
                list('abc'),
                {'verbose': True},
                ['Enumerate this:', (0, 'a'), (1, 'b'), (2, 'c')],
                marks=[],
            ),
            pytest.param(
                complex(2, 0),
                {'verbose': True},
                ('Better than complicated.', (2.0, 0.0)),
                marks=[],
            ),
        ],
    )
    def test_function(self, entrance, kwargs, expected, capsys):
        """Unittest."""
        capture = capsys.readouterr()
        assert pkg.fun(entrance, **kwargs) == expected
        assert capture.out == ''
