"""Test module."""

from incolume.academia_jedi import ajedi20250603_api_auth as pkg


class TestApiAuth:
    """Test class for API authentication."""

    def test_api_auth(self):
        """Test API authentication."""
        assert isinstance(pkg.auth_basic(), pkg.httpx.Response)
