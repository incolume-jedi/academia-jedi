"""Tests."""

import logging
from typing import ClassVar
import unittest
from dataclasses import is_dataclass

import pytest
from . import Product


class TestProductUnitTest(unittest.TestCase):
    """Test case unittest class."""

    def test_if_it_is_a_dataclass(self):
        """Unittest."""
        self.assertTrue(is_dataclass(Product))  # noqa: PT009

    def setUp(self):
        """Setup class test."""
        self.product = Product(1, 'test', 1.0, 10)

    def test_constructor(self):
        """Unittest."""
        self.assertEqual(self.product.id, 1)  # noqa: PT009
        self.assertEqual(self.product.name, 'test')  # noqa: PT009
        self.assertEqual(self.product.price, 1.0)  # noqa: PT009
        self.assertEqual(self.product.stock, 10)  # noqa: PT009

    def test_increse_stock(self):
        """Unittest."""
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 20)  # noqa: PT009

    def test_decrease_stock(self):
        """Unittest."""
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 0)  # noqa: PT009


class TestProductPytest:
    """Test case pytest class."""

    product: ClassVar = None

    def test_if_it_is_a_dataclass(self):
        """Unittest."""
        assert is_dataclass(Product)

    def setup_method(self, method):
        """Setup method."""
        logging.info('Setup for %s', method)
        self.product = Product(1, 'test', 1.0, 10)

    def teardown_method(self, method):
        """Setup method."""
        logging.info('Setup for %s', method)
        del self.product

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('id', 1),
            ('name', 'test'),
            ('price', 1.0),
            ('stock', 10),
        ],
    )
    def test_inicializador(self, entrance, expected):
        """Unittest."""
        assert getattr(self.product, entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (10, 20),
        ],
    )
    def test_increse_stock(self, entrance, expected):
        """Unittest."""
        self.product.increase_stock(entrance)
        assert self.product.stock == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (10, 0),
        ],
    )
    def test_decrease_stock(self, entrance, expected):
        """Unittest."""
        self.product.decrease_stock(entrance)
        assert self.product.stock == expected
