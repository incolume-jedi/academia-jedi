class Veiculo:
    """Class Veiculo."""
    def __init__(self, tipo: str = '') -> None:
        self.tipo = tipo

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.__dict__}'



if __name__ == '__main__':
    v = Veiculo('terrestre')
    # print(v, v.tipo)
    p = Veiculo('aquatico')
    print(v, p)