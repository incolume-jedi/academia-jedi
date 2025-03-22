"""Testes."""

from collections.abc import Callable
import incolume.academia_jedi.ajedi20250322_caos_academia as pkg
import pytest
from icecream import ic
from config import settings


ic.disable()
if settings.debug_mode:
    ic.enable()


@pytest.fixture()
def inst_academia():
    """TestClass.

    Fixture de metodo com setup e teardown.
    """
    # ic('setup')
    return pkg.Academia()
    # ic('teardown')


def test_academia(inst_academia):
    """Unittest."""
    assert isinstance(inst_academia, pkg.Academia)


@pytest.mark.parametrize(
    'func entrance expected'.split(),
    [
        (
            'halteres',
            {},
            [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
        ),
        (
            'porta_halteres',
            {},
            {
                10: 10,
                12: 12,
                14: 14,
                16: 16,
                18: 18,
                20: 20,
                22: 22,
                24: 24,
                26: 26,
                28: 28,
                30: 30,
                32: 32,
                34: 34,
                36: 36,
            },
        ),
        (
            'listar_halteres',
            {},
            [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
        ),
        (
            'calcular_caos',
            {},
            0,
        ),
        ('pegar_haltere', {'peso': 10}, 10),
        ('devolver_haltere', {'peso': 10, 'pos': 10}, None),
    ],
)
def test_academia(inst_academia, func, entrance, expected):
    """Unittest."""
    func = getattr(inst_academia, func)
    if isinstance(func, Callable):
        assert func(**entrance) == expected
    else:
        assert func == expected


def test_tipo():
    """Unittest."""
    assert {x.value: x.name for x in pkg.Tipo} == {
        1: 'organizado',
        2: 'desorganizado',
    }
