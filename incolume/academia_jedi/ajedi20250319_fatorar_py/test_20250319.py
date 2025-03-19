"""Tests."""

import unittest
from dataclasses import is_dataclass
from . import Product


class TestProduct(unittest.TestCase):
    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def setUp(self):
        self.product = Product(1, 'test', 1.0, 10)

    def test_constructor(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, 'test')
        self.assertEqual(self.product.price, 1.0)
        self.assertEqual(self.product.stock, 10)

    def test_increse_stock(self):
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 20)

    def test_decrease_stock(self):
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 0)
