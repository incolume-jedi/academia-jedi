"""Module."""

__author__ = '@britodfbr'  # pragma: no cover


class Real:
    """Real class."""

    def __init__(self, value: float) -> None:
        """Init class."""
        self.value = value

    def __repr__(self) -> str:
        """Method."""
        return f'R$ {self.value:0.2f}'

    def __add__(self, other):
        """Method."""
        return Real(self.value + other.value)

    def __gt__(self, other):
        """Method."""
        return self.value > other.value

    def __lt__(self, other):
        """Method."""
        return self.value < other.value
