"""Unit Test Module."""

__author__ = '@britodfbr'  # pragma: no cover

from exemplo1_abc import JSONHandler, PickleHandler, SerializedFileHandler
import pytest
from pathlib import Path
from tempfile import gettempdir


@pytest.fixture()
def fout():
    """Tempdir."""
    return Path(gettempdir()) / 'test-file.txt'


@pytest.fixture()
def data_test():
    """Data test."""
    return {'name': 'John Doe', 'age': 30}


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((PickleHandler, SerializedFileHandler), True),
        ((JSONHandler, SerializedFileHandler), True),
    ],
)
def test_type_handler(entrance, expected):
    """Test handler type."""
    assert issubclass(*entrance) == expected


@pytest.mark.parametrize(
    'suffix handler'.split(),
    [
        ('.pkl', PickleHandler),
        ('.json', JSONHandler),
    ],
)
def test_write_file(fout, data_test, suffix, handler):
    """Test if write file."""
    output_file = fout.with_suffix(suffix)
    file_handler = handler(output_file)
    file_handler.write(data_test)
    assert output_file.is_file()


@pytest.mark.parametrize(
    'suffix handler'.split(),
    [
        ('.pkl', PickleHandler),
        ('.json', JSONHandler),
    ],
)
def test_read_file(fout, data_test, suffix, handler):
    """Test if readible file."""
    output_file = fout.with_suffix(suffix)
    file_handler = handler(output_file)
    assert file_handler.read() == data_test
