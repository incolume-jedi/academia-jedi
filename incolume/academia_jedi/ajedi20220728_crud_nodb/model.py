"""model package."""

from dataclasses import dataclass, field
from datetime import datetime


def gen_id(initial: int = 1) -> int:
    """Generate id function."""
    count = initial or 1
    while True:
        yield count
        count += 1


a = gen_id()


def get_id():
    """Get id next."""
    return next(a)


@dataclass
class Pessoa:
    """Class Pessoa."""

    nome: str
    date_born: datetime
    id: int = field(init=False, default_factory=get_id)
    email: list[str] = field(default_factory=list)
    telefone: list[str] = field(default_factory=list)
    address: list[str] = field(default_factory=list)

    def to_dict(self):
        """Return self.dict."""
        return self.__dict__


if __name__ == '__main__':
    for i in range(10):
        print(get_id())
