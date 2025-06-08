"""Test module."""

from typing import NoReturn
import pytest
import re
from incolume.academia_jedi.ajedi20221212_python_regex_search_replace import (
    convert_case,
)


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('jOE kIM mAx ABY lIzA', 'Joe Kim MaX aby LiZa'),
        ('bRASIL!@$', 'Brasil!@$'),
    ],
)
def test_re_search_replace(entrance, expected) -> NoReturn:
    """Unittest."""
    assert re.sub(r'([A-Z]+)|([a-z]+)', convert_case, entrance) == expected
