"""Test Module."""

from pathlib import Path
import shutil
from tempfile import gettempdir
from typing import ClassVar
from icecream import ic
from . import getssh, get_uuid, get_uid
import httpx
import requests
import pytest


@pytest.fixture(autouse=True)
def no_httpx(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    # monkeypatch.delattr('httpx.sessions.Session.request') # noqa: ERA001


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr('requests.sessions.Session.request')


class MockResponse:
    """Custom class to be the mock return value.

    will override the object.Response returned from (httpx|requests).get

    mock json() method always returns a specific testing dictionary
    """

    @staticmethod
    def json():
        """Json fake method."""
        return {'mock_key': 'mock_response'}


class TestMonkeyPatch:
    """TestMonkeyPatch class."""

    PATH: ClassVar[Path] = None

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.PATH = Path(gettempdir()).joinpath(cls.__name__)
        ic(cls.PATH)
        cls.PATH.mkdir(
            parents=True,
            exist_ok=True,
        )

    @classmethod
    def teardown_class(cls):
        """Teardown class.

        Teardown da classe. Remove todos os arquivos
         e diretórios gerados ao final.
        """
        shutil.rmtree(cls.PATH)

    def test_getssh(self, monkeypatch):
        """Unittest."""
        # Application of the monkeypatch to replace Path.home
        # with the behavior of lambda defined above.
        monkeypatch.setattr(Path, 'home', lambda: self.PATH / 'abc')

        # Calling getssh() will use mockreturn in place of Path.home
        # for this test with the monkeypatch.
        x = getssh()
        assert x == self.PATH / 'abc/.ssh'

    def test_get_uid(self, monkeypatch):
        """Unittest."""

        # apply the monkeypatch for requests.get to mock_get
        def mock_get(*args, **kwargs):
            """Mockget."""
            ic(args, kwargs)
            return MockResponse()

        monkeypatch.setattr(
            requests,
            'get',
            mock_get,
        )

        # app.get_json, which contains requests.get, uses the monkeypatch
        result = get_uid()
        assert result['mock_key'] == 'mock_response'

    def test_get_uuid(self, monkeypatch):
        """Unittest."""
        # apply the monkeypatch for requests.get to mock_get
        monkeypatch.setattr(
            httpx,
            'get',
            lambda *args, **kwargs: MockResponse(),  # noqa: ARG005
        )

        # app.get_json, which contains requests.get, uses the monkeypatch
        result = get_uuid()
        assert result['mock_key'] == 'mock_response'
