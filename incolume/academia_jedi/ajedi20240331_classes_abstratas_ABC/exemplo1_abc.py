"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from abc import ABC, abstractmethod
from pathlib import Path
from pickle import dumps as pickle_dumps, loads as pickle_loads
from json import dumps as json_dumps, loads as json_loads
import logging
from tempfile import gettempdir

logging.basicConfig(
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
    level=logging.INFO,
)


class SerializedFileHandler(ABC):
    """Abstract class for serialize files."""

    def __init__(self, filename: Path):
        """Init class."""
        self.filename = Path(filename)

    @abstractmethod
    def serialize(self, data):
        """Serialize logical for handler file."""

    @abstractmethod
    def deserialize(self, data):
        """Deserialize logical for handler file."""

    def write(self, data):
        """Write file handler."""
        with self.filename.open('wb') as file:
            file.write(self.serialize(data))

    def read(self):
        """Read file handler."""
        with self.filename.open('rb') as file:
            return self.deserialize(file.read())


class PickleHandler(SerializedFileHandler):
    """Class handler for pickle files."""

    def serialize(self, data):
        """Serialize logical for handler pickle file."""
        logging.info('Output into %s', self.filename)
        return pickle_dumps(data)

    def deserialize(self, data):
        """Deserialize logical for handler pickle file."""
        logging.info('Read from %s', self.filename)
        return pickle_loads(data)  # noqa: S301 suspicious-pickle-usage


class JSONHandler(SerializedFileHandler):
    """Class handler for json files."""

    def serialize(self, data):
        """Serialize logical for handler json file."""
        logging.info('Output into %s', self.filename)
        return json_dumps(data).encode('utf-8')

    def deserialize(self, data):
        """Deserialize logical for handler json file."""
        logging.info('Read from %s', self.filename)
        return json_loads(data.decode('utf-8'))


def main():
    """Run it."""
    data = {'name': 'John Doe', 'age': 30}
    dout = Path(gettempdir())

    pickle_writer = PickleHandler(dout / 'data.pkl')
    pickle_writer.write(data)
    logging.info(pickle_writer.read())

    json_writer = JSONHandler(dout / 'data.json')
    json_writer.write(data)
    logging.info(json_writer.read())

    assert isinstance(pickle_writer, SerializedFileHandler)  # noqa: S101
    assert isinstance(json_writer, SerializedFileHandler)  # noqa: S101


if __name__ == '__main__':
    main()
