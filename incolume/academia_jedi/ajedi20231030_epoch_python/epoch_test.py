"""Academia20231030."""

from datetime import datetime

import pytest
import pytz
import incolume.academia_jedi.ajedi20231030_epoch_python.epoch_python as pkg


@pytest.mark.parametrize(
    'entrance', 'expected',
    [
        (datetime(2023, 10, 30, 19, 4, 7, tzinfo = pytz.timezone('America/Sao_Paulo')), 1698703447),
        (datetime(2023, 9, 30, 19, 4, 7, tzinfo = pytz.timezone('America/Sao_Paulo')), 1696111447),
        (datetime(2023, 5, 28, 20, 4, 7, tzinfo = pytz.timezone('America/Sao_Paulo')), 1685315047),
        (datetime(2004, 9, 23, 0, 5, 1), 1095908701),
    ],
)
def test_gerador_epoch(entrance, expected) -> None:
    """Testa função gerador epoch."""
    assert pkg.gerador_epoch(entrance) == expected


@pytest.mark.parametrize(
    'entrance', 'expected',
    [
        (1698703447, (2023, 10, 30, 19, 4, 7)),
        (1696111447, (2023, 9, 30, 19, 4, 7)),
        (1685315047, (2023, 5, 28, 20, 4, 7)),
        (1095908701, (2004, 9, 23, 0, 5, 1)),
    ],
)
def test_reverter_epoch(entrance, expected) -> None:
    """Testa a função reverter epoch."""
    assert pkg.reverter_epoch(entrance) == datetime(*expected)
