"""Exemplo protocol.

disponivel em https://github.com/ArjanCodes/examples/
blob/main/2024/protocol/protocol_as_abc.py
"""

import abc
import json
import logging
from pathlib import Path
from tempfile import gettempdir
from typing import Protocol


class Writable(Protocol):
    """Writeble with abstract method."""

    @abc.abstractmethod
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    """Readable with abstract method."""

    @abc.abstractmethod
    def read(self) -> dict:
        """This method should return a dictionary."""


class JsonHandler(Readable, Writable):
    """Readable and writeble with abstract method."""

    def __init__(self, filename: Path):
        """Init Handler."""
        self.filename: Path = filename

    def read(self) -> dict:
        """Deserialize logical for handler json file."""
        logging.info('Read from %s', self.filename)
        with self.filename.open('rb') as f:
            return json.load(f)

    def write(self, data: dict) -> bytes:
        """Write some data."""
        logging.info('Output into %s', self.filename)
        with self.filename.open('wb') as f:
            f.write(json.dumps(data).encode('utf-8'))

    def __str__(self):
        """Magic method dunder str."""
        return f'{self.__class__.__name__}()'


def main():
    """Run it."""
    data = {'name': 'John Doe', 'age': 30}
    handlers = JsonHandler(Path(gettempdir()) / 'data_protocol.json')
    handlers.write(data)
    print(handlers.read())


if __name__ == '__main__':
    main()
