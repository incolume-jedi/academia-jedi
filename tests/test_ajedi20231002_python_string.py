import pytest

from incolume.academia_jedi.ajedi20231002_python_string import (
    python_string,
    python_string0,
)


def test_python_string():
    """Verificar se retorna 'Python' ao contrário"""
    assert python_string('Python') == 'nohtyP'


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('ana', 'ana'),
        ('xpto', 'otpx'),
        ('carro', 'orrac'),
        ('girafa', 'afarig'),
        ('fghuio', 'oiuhgf'),
        ('299792458', '854297992'),
    ],
)
def test_python_string0(entrance, expected):
    """Verificar se retorna string ao contrário"""
    assert python_string0(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('ana', 'ana'),
        ('xpto', 'otpx'),
        ('carro', 'orrac'),
        ('girafa', 'afarig'),
        ('fghuio', 'oiuhgf'),
        ('299792458', '854297992'),
    ],
)
def test_python_string_1(entrance, expected):
    """Verificar se retorna string ao contrário"""
    assert python_string(entrance) == expected
