"""Module."""

from typing import NoReturn, Protocol


class Writable(Protocol):
    """Writable class."""

    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    """Readable class."""

    def read(self) -> dict:
        """This method should return a dictionary."""


class ReadWritable(Readable, Writable):
    """ReadWritable class."""

    def __str__(self):
        """Method dunder str."""
        return f'{self.__class__.__name__}()'


def main() -> NoReturn:
    """Run it."""
    data = {'name': 'John Doe', 'age': 30}
    handlers = ReadWritable()
    handlers.write(data)
    print(handlers.read())


if __name__ == '__main__':
    main()
