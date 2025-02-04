"""Module."""

from __future__ import annotations

import pytest
import pytz
import equality
import formatly
import agregate
import datetime as dt
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293


@pytest.mark.parametrize(
    'fruit1 fruit2 expected'.split(),
    [
        (
            equality.Fruit0(name='Apple', grams=100),
            equality.Fruit0(name='Orange', grams=150),
            False,
        ),
        (
            equality.Fruit0(name='Apple', grams=100),
            equality.Fruit0(name='Apple', grams=80),
            True,
        ),
    ],
)
def test_equality_fruit0(fruit1, fruit2, expected):
    """Compare Fruits."""
    assert (fruit1 == fruit2) == expected


@pytest.mark.parametrize(
    'fruit1 fruit2 expected'.split(),
    [
        (
            equality.Fruit1(name='Apple', grams=100),
            equality.Fruit1(name='Orange', grams=150),
            False,
        ),
        (
            equality.Fruit1(name='Apple', grams=100),
            equality.Fruit1(name='Apple', grams=80),
            False,
        ),
        (
            equality.Fruit1(
                name='Apple',
                grams=100,
                date=dt.datetime(
                    2024,
                    4,
                    8,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            equality.Fruit1(
                name='Apple',
                grams=100,
                date=dt.datetime(
                    2024,
                    4,
                    8,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            True,
        ),
        (
            equality.Fruit1(
                name='Apple',
                grams=100,
                date=dt.datetime(
                    2024,
                    4,
                    8,
                    7,
                    0,
                    0,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            equality.Fruit1(
                name='Apple',
                grams=100,
                date=dt.datetime(
                    2024,
                    4,
                    8,
                    7,
                    0,
                    1,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            False,
        ),
    ],
)
def test_equality_fruit1(fruit1, fruit2, expected):
    """Compare Fruits."""
    assert (fruit1 == fruit2) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (formatly.Fruit2(name='Apple', grams=2350), '2.35Kg'),
        (formatly.Fruit2(name='Apple', grams=2000), '2.00Kg'),
        (formatly.Fruit2(name='Apple', grams=5359), '5.36Kg'),
    ],
)
def test_formatly_fruit2_kg(entrance, expected):
    """Test format showed."""
    assert f'{entrance:kg}' == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            formatly.Fruit2(
                name='Apple',
                grams=2350,
                date=dt.datetime(
                    1978,
                    6,
                    20,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            '2.35Kg (2350g) de Apple em 1978-06-20T00:00:00-03:06',
        ),
        (
            formatly.Fruit2(
                name='Apple',
                grams=2000,
                date=dt.datetime(
                    1978,
                    6,
                    20,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            '2.00Kg (2000g) de Apple em 1978-06-20T00:00:00-03:06',
        ),
        (
            formatly.Fruit2(
                name='Apple',
                grams=5359,
                date=dt.datetime(
                    1978,
                    6,
                    20,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            '5.36Kg (5359g) de Apple em 1978-06-20T00:00:00-03:06',
        ),
    ],
)
def test_formatly_fruit2_desc(entrance, expected):
    """Test format showed."""
    assert f'{entrance:desc}' == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        pytest.param(
            agregate.Fruit3(
                name='Apple',
                grams=2350,
                date=dt.datetime(
                    1978,
                    6,
                    20,
                    tzinfo=pytz.timezone(settings.tz),
                ),
            ),
            '2.35Kg (2350g) de Apple em 1978-06-20T00:00:00-03:06',
            marks=pytest.mark.skip(
                reason="AttributeError: 'str'"
                " object has no attribute 'isoformat'",
            ),
        ),
    ],
)
def test_agregate_fruit3_desc(entrance, expected):
    """Unit test."""
    assert f'{entrance:desc}' == expected


@pytest.mark.parametrize(
    'entrance fruits expected'.split(),
    [
        pytest.param(
            'apple',
            (
                agregate.Fruit3(
                    name='Apple',
                    grams=2350,
                    date=dt.datetime(
                        1978,
                        6,
                        20,
                        0,
                        1,
                        23,
                        456789,
                        tzinfo=pytz.timezone(settings.tz),
                    ),
                ),
                agregate.Fruit3(
                    name='orange',
                    grams=2350,
                    date=dt.datetime(
                        1978,
                        6,
                        20,
                        0,
                        1,
                        23,
                        456789,
                        tzinfo=pytz.timezone(settings.tz),
                    ),
                ),
                agregate.Fruit3(
                    name='Apple',
                    grams=500,
                    date=dt.datetime(
                        1978,
                        6,
                        20,
                        0,
                        1,
                        23,
                        456789,
                        tzinfo=pytz.timezone(settings.tz),
                    ),
                ),
                agregate.Fruit3(
                    name='pineApple',
                    grams=350,
                    date=dt.datetime(
                        1978,
                        6,
                        20,
                        0,
                        1,
                        23,
                        456789,
                        tzinfo=pytz.timezone(settings.tz),
                    ),
                ),
            ),
            [
                '2.35Kg (2350g) de Apple em 1978-06-20T00:01:23.456789-03:06',
                '0.50Kg (500g) de Apple em 1978-06-20T00:01:23.456789-03:06',
            ],
            marks=[
                pytest.mark.skip(reason='comparação objeto e str'),
            ],
        ),
    ],
)
def test_agregate_fruit3_handler(entrance, fruits, expected):
    """Test handler."""
    basket = agregate.Basket(fruits)
    assert basket[entrance] == expected
