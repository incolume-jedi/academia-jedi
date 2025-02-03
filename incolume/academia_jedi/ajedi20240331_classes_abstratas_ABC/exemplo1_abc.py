"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

__author__ = '@britodfbr'  # pragma: no cover

import logging
from abc import ABC, abstractmethod
from json import dumps as json_dumps
from json import loads as json_loads
from pathlib import Path
from pickle import dumps as pickle_dumps
from pickle import loads as pickle_loads
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
        return pickle_loads(data)  # suspicious-pickle-usage


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

    assert isinstance(pickle_writer, SerializedFileHandler)
    assert isinstance(json_writer, SerializedFileHandler)


if __name__ == '__main__':
    main()
