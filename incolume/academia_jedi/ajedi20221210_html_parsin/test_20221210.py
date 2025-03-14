"""Test module."""

from typing import NoReturn
import pytest
import requests
from incolume.academia_jedi.ajedi20221210_html_parsin import (
    bs4_parsing as bp,
    parsel_parsing as pp,
    selectolax_parsing as sp,
    config,
    resp,
)


class TestCase:
    """TestCase."""

    def test_config_exists(self) -> NoReturn:
        """Unittest."""
        assert config.exists()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(bp.resp, True, marks=[]),
            pytest.param(pp.resp, True, marks=[]),
            pytest.param(sp.resp, True, marks=[]),
            pytest.param(resp, True, marks=[]),
        ],
    )
    def test_resp_response(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert isinstance(entrance, requests.Response) is expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(bp.resp, 200, marks=[]),
            pytest.param(pp.resp, 200, marks=[]),
            pytest.param(sp.resp, 200, marks=[]),
            pytest.param(resp, 200, marks=[]),
        ],
    )
    def test_resp_status(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert entrance.status_code == expected
