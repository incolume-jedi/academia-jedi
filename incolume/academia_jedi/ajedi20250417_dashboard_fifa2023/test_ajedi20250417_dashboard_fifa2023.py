"""Test Dashboard FIFA2023."""

from typing import NoReturn
from incolume.academia_jedi.ajedi20250417_dashboard_fifa2023 import URLS


class TestDashboard:
    """Case tests."""

    def test_urls(self) -> NoReturn:
        """Unittest."""
        assert URLS.__annotations__ == ''
