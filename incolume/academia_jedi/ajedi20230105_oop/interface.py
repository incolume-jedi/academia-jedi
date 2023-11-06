class Fruta:
    def __init__(self, nome: str = '', peso: float = 0.1) -> None:
        self.peso = peso
        self.nome = nome or 'fruta'

    def __str__(self) -> str:
        return '{nome}({peso} kg)'.format(**self.__dict__)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return '({x}, {y})'.format(**self.__dict__)

    def __str__(self) -> str:
        return f'Point({self.x}, {self.y})'
