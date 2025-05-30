import io

# ruff: noqa: D100, D101, D103, ERA001, S101
from typing import Protocol, runtime_checkable


@runtime_checkable
class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


def main():
    io_writer = io.BytesIO()

    assert isinstance(io_writer, Writable)

    # io_writer.write({'name': 'John Doe', 'age': 30})


if __name__ == '__main__':
    main()
