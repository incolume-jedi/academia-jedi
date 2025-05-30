"""Test module."""

import platform
import pytest
from incolume.academia_jedi.ajedi20231213_aspose_pkg import (
    prospect_aspose as pkg,
)
import re


@pytest.mark.skipif(
    condition=platform.python_version() >= '3.12.0',
    reason='Dont run in Python3.12+',
)
@pytest.mark.parametrize(
    ['entrance', 'regex'],
    [
        pytest.param({}, '.*tmp.*', marks=()),
        pytest.param({'prefix': 'file_'}, '.*file_.*', marks=()),
        pytest.param(
            {'suffix': '.docx'},
            '.*.docx$',
        ),
        pytest.param(
            {'prefix': 'test-', 'suffix': '.pdf'},
            '.*test-.+pdf$',
        ),
    ],
)
def test_new_file(entrance: dict, regex: str) -> None:
    """Test it."""
    assert re.match(
        regex,
        pkg.new_filename(**entrance).as_posix(),
        flags=re.IGNORECASE,
    )
