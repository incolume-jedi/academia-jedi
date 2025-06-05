"""Test module."""

import pytest
from incolume.academia_jedi import ajedi20250603_api_auth as pkg


class TestApiAuth:
    """Test class for API authentication."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, {}),
            pytest.param(
                {'user': 'u171'},
                {
                    'expected_exception': pkg.httpx.HTTPStatusError,
                    'match': "Client error '401 UNAUTHORIZED' for url 'https://httpbin.org/basic-auth/username/password'",
                },
            ),
            pytest.param({'pw': '12345678'}, {}),
            pytest.param(
                {
                    'user': 'root',
                    'pw': '123456',
                    'url': 'https://httpbin.org/basic-auth/root/123456',
                },
                {},
            ),
        ],
    )
    def test_api_auth(self, entrance, expected):
        """Test API authentication."""
        result = pkg.auth_basic(**entrance)
        assert isinstance(result, pkg.httpx.Response)
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                result.raise_for_status()
        else:
            assert result.json().get('authenticated')
