"""Accolade module."""

from icecream import ic


class Accolade:
    """Accolade class."""

    def __init__(self, function):
        """Initializer."""
        self.function = function

    def __call__(self, name):
        """Adding Excellency before name."""
        name = 'Excellency ' + name
        self.function(name)
        # Saluting after the name
        ic(f'Thanks {name} for gracing the occasion')
