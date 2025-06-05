"""Test module."""

import pytest
from incolume.academia_jedi import ajedi20250603_api_auth as pkg
from http import HTTPStatus
from config import settings


class TestApiAuth:
    """Test class for API authentication."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
                {},
                marks=[pytest.mark.xfail(reason='Expected 200 OK')],
            ),
            pytest.param(
                {'user': 'u171'},
                {
                    'expected_exception': pkg.httpx.HTTPStatusError,
                    'match': "Client error '401 UNAUTHORIZED' for url 'https://httpbin.org/basic-auth/username/password'",
                },
                marks=[pytest.mark.xfail(reason='Expected 401 Unauthorized')],
            ),
            pytest.param(
                {'pw': '12345678'},
                {},
                marks=[pytest.mark.xfail(reason='Expected 401 Unauthorized')],
            ),
            pytest.param(
                {
                    'user': 'root',
                    'pw': '123456',
                    'url': 'https://httpbin.org/basic-auth/root/123456',
                },
                {},
                marks=[pytest.mark.xfail(reason='Expected 200 OK')],
            ),
        ],
    )
    def test_api_auth(self, entrance, expected):
        """Test API authentication."""
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                pkg.auth_basic(**entrance)
        else:
            result = pkg.auth_basic(**entrance)
            assert isinstance(result, pkg.httpx.Response)
            assert result.json().get('authenticated')

    def test_auth_token(self):
        """Test token authentication."""
        result = pkg.auth_token(
            city='Brasília',
            token=settings.OPEN_WEATHER_API_KEY,
        )
        assert isinstance(result, pkg.httpx.Response)
        assert result.status_code == HTTPStatus.OK
        assert 'weather' in result.json()
        assert 'main' in result.json()
        assert 'temp' in result.json()['main']
