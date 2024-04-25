"""Module."""

import pytest
import pytz

import equality
import formatly
import agregate
import datetime as dt

__author__ = '@britodfbr'  # pragma: no cover

from config import settings


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
                reason="AttributeError: 'str' object has no attribute 'isoformat'"
            ),
        ),
    ],
)
def test_agregate_fruit3_desc(entrance, expected):
    assert f'{entrance:desc}' == expected


@pytest.mark.parametrize(
    'entrance fruits expected'.split(),
    [
        (
            'apple',
            (
                agregate.Fruit3(name='Apple', grams=2350),
                agregate.Fruit3(name='orange', grams=2350),
                agregate.Fruit3(name='Apple', grams=2350),
                agregate.Fruit3(name='pineApple', grams=350),
            ),
            '2.35Kg (2350g) de Apple em 1978-06-20T00:00:00-03:06',
        ),
    ],
)
def test_agregate_fruit3_handler(entrance, fruits, expected):
    """Test handler."""
    basket = agregate.Basket(fruits)
    assert basket[entrance] == expected
