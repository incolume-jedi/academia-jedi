"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from abc import ABC, abstractmethod
from json import dumps as json_dumps
from json import loads as json_loads
from pickle import dumps as pickle_dumps
from pickle import loads as pickle_loads
from typing import Protocol

# ruff: noqa: A002, ANN001, ANN201, ARG001, ARG002, BLE001, C901, D101, D102, D103, D107, DTZ003,DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class SerializedFileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(self.serialize(data))

    def read(self):
        with open(self.filename, 'rb') as file:
            return self.deserialize(file.read())


class PickleHandler(SerializedFileHandler):
    def serialize(self, data):
        return pickle_dumps(data)

    def deserialize(self, data):
        return pickle_loads(data)


class JSONHandler(SerializedFileHandler):
    def serialize(self, data):
        return json_dumps(data).encode()

    def deserialize(self, data):
        return json_loads(data.decode())


class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    def read(self) -> dict:
        """This method should return a dictionary."""


def write(handler: Writable, data: dict) -> None:
    handler.write(data)


def read(handler: Readable) -> dict:
    return handler.read()


def main():
    data = {'name': 'John Doe', 'age': 30}
    pickle_writer = PickleHandler('../data.pkl')
    write(pickle_writer, data)
    print(read(pickle_writer))

    json_writer = JSONHandler('../data.json')
    write(json_writer, data)
    print(read(json_writer))

    assert isinstance(pickle_writer, Writable)
    assert isinstance(json_writer, Readable)


if __name__ == '__main__':
    main()
