"""Modulo de classes."""


class Fruta:
    """Fruta class."""

    def __init__(self, nome: str = '', peso: float = 0.1) -> None:
        """Init class."""
        self.peso = peso
        self.nome = nome or 'fruta'

    def __str__(self) -> str:
        """Str class."""
        return '{nome}({peso} kg)'.format(**self.__dict__)


class Point:
    """Point class."""

    def __init__(self, x: int, y: int) -> None:
        """Init class."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Repr class."""
        return '({x}, {y})'.format(**self.__dict__)

    def __str__(self) -> str:
        """Str class."""
        return f'Point({self.x}, {self.y})'
