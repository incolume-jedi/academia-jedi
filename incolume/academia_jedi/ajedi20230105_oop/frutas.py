import interface


class Manga(interface.Fruta):
    def __init__(self, peso: float):
        self.nome = 'Manga'
        self.peso = peso


class Uva(interface.Fruta):
    def __init__(self, peso: float = 0.1):
        super().__init__('Uva', peso)
