"""Module."""

from __future__ import annotations

import sys
from dataclasses import dataclass

if sys.version_info < (3, 12):
    from typing_extensions import Self
else:
    from typing import Self

msgs: dict = {
    'number_positive': 'Number must be positive',
    'stock_negative': 'Stock must be greater than or equal to 0',
}


@dataclass()
class Product:
    """Product class."""

    id: int
    name: str
    price: float
    stock: int

    def increase_stock(self, stock_to_add: int) -> Self:
        """Increase stock."""
        self.check_positive_number(stock_to_add)
        self.stock: int = self.stock + stock_to_add
        return self

    def decrease_stock(self, stock_to_reduce: int) -> Self:
        """Decrease stock."""
        self.check_positive_number(stock_to_reduce)
        new_stock = self.stock - stock_to_reduce
        self.check_negative_stock(new_stock)
        self.stock = self.stock - stock_to_reduce
        return self

    def check_positive_number(self, value: int) -> None:
        """Check positive number."""
        if value <= 0:
            raise ValueError(msgs['number_positive'])

    def check_negative_stock(self, value: int) -> None:
        """Check negative stock."""
        if value < 0:
            raise ValueError(msgs['stock_negative'])
