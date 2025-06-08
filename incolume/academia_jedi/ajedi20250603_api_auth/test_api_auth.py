"""Test module."""

import pytest
from incolume.academia_jedi import ajedi20250603_api_auth as pkg
from http import HTTPStatus
from config import settings
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent / 'dotenv')


class TestApiAuth:
    """Test class for API authentication."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
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
            token=os.environ['OPEN_WEATHER_API_KEY']
            or settings.OPEN_WEATHER_MAP_API_KEY,
        )
        assert isinstance(result, pkg.httpx.Response)
        assert result.status_code == HTTPStatus.OK
        assert 'weather' in result.json()
        assert 'main' in result.json()
        assert 'temp' in result.json()['main']

    def test_auth_bearer(self):
        """Test Bearer token authentication."""
        assert {
            'access_token',
            'expires_in',
            'token_type',
        }.issubset(pkg.get_bearer().json().keys())

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                {},
                HTTPStatus.UNAUTHORIZED.value,
                marks=[],
            ),
            pytest.param(
                {
                    'token': pkg.get_bearer().json().get('access_token'),
                    'artist_id': '0gO5Vbklho8yrBrUdHhuLH',  # Oficina G3
                },
                HTTPStatus.OK.value,
                marks=[],
            ),
            pytest.param(
                {
                    'token': pkg.get_bearer().json().get('access_token'),
                    'artist_id': '2aKyKSggb31Kw9s9i3iXoo',  # Aline Barros
                },
                HTTPStatus.OK.value,
                marks=[],
            ),
        ],
    )
    def test_get_spotify(self, entrance, expected):
        """Test Spotify token retrieval."""
        response = pkg.get_spotify(**entrance)
        assert response.status_code == expected
