__author__ = '@britodfbr'  # pragma: no cover


class Real:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'R$ {self.value:0.2f}'

    def __add__(self, other):
        return Real(self.value + other.value)

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value
