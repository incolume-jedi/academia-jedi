"""Test module."""

from typing import NoReturn
import pytest
from incolume.academia_jedi.ajedi20221210_html_parsin import (
    bs4_parsing as bp,
    parsel_parsing as pp,
    selectolax_parsing as sp,
    config,
)


class TestCase:
    """TestCase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(bp.config, True, marks=[]),
            pytest.param(pp.config, True, marks=[]),
            pytest.param(sp.config, True, marks=[]),
            pytest.param(config, True, marks=[]),
        ],
    )
    def test_config_exists(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert entrance.exists(), f'Error: {entrance}' is expected
