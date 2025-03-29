"""Modulo de heraça."""

import interface


class Manga(interface.Fruta):
    """Manga class."""

    def __init__(self, peso: float) -> None:
        """Init class."""
        self.nome = 'Manga'
        self.peso = peso


class Uva(interface.Fruta):
    """Uva class."""

    def __init__(self, peso: float = 0.1) -> None:
        """Init class."""
        super().__init__('Uva', peso)
