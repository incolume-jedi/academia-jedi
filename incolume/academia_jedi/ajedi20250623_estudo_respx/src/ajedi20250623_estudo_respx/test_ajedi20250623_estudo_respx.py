"""Test module."""

from . import URL
import httpx
import respx
from http import HTTPStatus
import pytest


class TestStudiesRespx:
    """Test class for respx studies."""

    @respx.mock
    def test_decorator(self):
        """Test decorator with respx."""
        my_route = respx.get(URL)
        response = httpx.get(URL)
        assert my_route.called
        assert response.status_code == HTTPStatus.OK
        assert response.status_code == httpx.codes.OK

    def test_context(self):
        """Test context manager with respx."""
        with respx.mock:
            my_route = respx.get(URL)
            response = httpx.get(URL)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK
            assert response.status_code == httpx.codes.OK

    def test_fixture(self, respx_mock):
        """Test fixture with respx."""
        my_route = respx_mock.get(URL)
        response = httpx.get(URL)
        assert my_route.called
        assert response.status_code == httpx.codes.OK

    @pytest.mark.skip
    @respx.mock(base_url=URL)
    async def test_something(self, respx_mock):
        """Test something with respx."""
        async with httpx.AsyncClient(base_url=URL) as client:
            respx_mock.get('/get/').mock(
                return_value=httpx.Response(httpx.codes.OK, text='Baz'),
            )
            response = await client.get('/get')
            assert response.text == 'Baz'
