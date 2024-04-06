"""Test module."""
import pytest
from incolumepy.utils.files import realfilename
from incolumepy.utils.numerical import milhar


__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrada',
    [
        'texto.txt',
    ],
)
def test_files(entrada):
    """Criação de arquivos."""
    file = realfilename(entrada, ext='html')
    file.write_text('xpto')
    assert file.is_file()


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('1', '1'),
        ('10', '10'),
        ('100', '100'),
        ('1000', '1.000'),
        ('1000000000000000000000000', '1.000.000.000.000.000.000.000.000'),
        ('100000000000000000000000000000000000000000000000000000000000000000',
         '100.000.000.000.000.000.000.000.000.000.000.000.000.'
         '000.000.000.000.000.000.000.000.000'),
        # (re.sub(r'[ \.]+', '', '1.954 891'), '1.954.891'),
    ],
)
def test_milhar(entrance, expected):
    """Exemplo milhar."""
    assert milhar(entrance) == expected



