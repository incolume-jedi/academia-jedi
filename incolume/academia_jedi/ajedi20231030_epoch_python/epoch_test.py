"""Academia20231030."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from datetime import datetime

import pytest
import pytz
import incolume.academia_jedi.ajedi20231030_epoch_python.epoch_python as pkg


@pytest.mark.parametrize(
    'entrance',
    'expected',
    [
        (
            datetime(
                2023,
                10,
                30,
                19,
                4,
                7,
                tzinfo=pytz.timezone('America/Sao_Paulo'),
            ),
            1698703447,
        ),
        (
            datetime(
                2023,
                9,
                30,
                19,
                4,
                7,
                tzinfo=pytz.timezone('America/Sao_Paulo'),
            ),
            1696111447,
        ),
        (
            datetime(
                2023,
                5,
                28,
                20,
                4,
                7,
                tzinfo=pytz.timezone('America/Sao_Paulo'),
            ),
            1685315047,
        ),
        (datetime(2004, 9, 23, 0, 5, 1), 1095908701),
    ],
)
def test_gerador_epoch(entrance, expected) -> None:
    """Testa função gerador epoch."""
    assert pkg.gerador_epoch(entrance) == expected


@pytest.mark.parametrize(
    'entrance',
    'expected',
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
