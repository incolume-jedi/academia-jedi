import pytest
from incolume.academia_jedi.ajedi20231213_aspose_pkg import prospect_aspose as pkg
import re


@pytest.mark.parametrize(
    'entrance regex'.split(),
    [
        pytest.param({}, '.*tmp.*', marks=()),
        pytest.param({'prefix': 'file_'}, '.*file_.*', marks=()),
        pytest.param({'suffix': '.docx'},'.*.docx$',),
        pytest.param({'prefix': 'test-', 'suffix': '.pdf'}, '.*test-.+pdf$', ),
    ]
)
def test_new_file(entrance: dict, regex: str) -> None:
    """Test it."""

    assert re.match(regex, pkg.new_filename(**entrance).as_posix(), flags=re.I)