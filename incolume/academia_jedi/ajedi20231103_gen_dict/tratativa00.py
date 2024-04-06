from dataclasses import dataclass


class Veiculo:
    """Class Veiculo."""
    def __init__(self, tipo: str = '') -> None:
        self.tipo = tipo

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'

@dataclass
class Vehicle:
    """Class Vehicle."""
    tipo: str = ''
    _chassi: str = ''
    __velocidade: float = 0.0

    @property
    def velocidade(self):
        """Acelerar."""
        return self.__velocidade

    @property
    def acelerar(self) -> None:
        """Acelerar"""

    @acelerar.setter
    def acelerar(self, value: float = 0) -> None:
        """Acelerar."""
        self.__velocidade = max(0, value)


if __name__ == '__main__':
    v = Veiculo('terrestre')
    # print(v, v.tipo)
    p = Veiculo('aquatico')
    print(v, p.tipo)

    a = Vehicle()
    b = Vehicle('terrestre')
    c = Vehicle('aério')
    print(a, b, c)
    a.tipo = 'aquatico'
    print(a, b, c)
    a._chassi = 'lasdjfhalkdjsfhalksdjfhalsdfa8sdfasd7f6a7sdf6asd7f'
    print(a, b, c)
    a.__velocidade = 100.0
    print(a, b, c)

    a.acelerar = 100
    print(a.velocidade, a.acelerar)


