"""Email with python."""

import pytest
import incolume.academia_jedi.ajedi20250430_py_email as pkg
from pathlib import Path
from tempfile import gettempdir
import inspect
import json
import shutil


class TestPyEmail:
    """Test the ajedi20250430_py_email package.

    This class contains test methods for the ajedi20250430_py_email package.
    """

    path_class: Path = Path(
        gettempdir(),
        inspect.stack()[0][3],
    )
    credentials_file: Path = path_class / 'credentials/credentials.json'
    credentials: dict[str, str] = {
        'email': 'dev@example.com',
        'google_password': 'xpto',
    }

    @classmethod
    def setup_method(cls):
        """Setup method.

        This method is called before for set up the test environment.
        """
        cls.credentials_file.parent.mkdir(parents=True, exist_ok=True)
        cls.credentials_file.write_text(
            json.dumps(cls.credentials),
            encoding='utf-8',
        )

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        shutil.rmtree(cls.path_class, ignore_errors=True)

    def test_import(self):
        """Test the import of the ajedi20250430_py_email package."""
        assert pkg.__name__ == 'incolume.academia_jedi.ajedi20250430_py_email'

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(pkg.CREDENTIALS_PATH),
            pytest.param(credentials_file),
        ],
    )
    def test_credentials_path(self, entrance):
        """Test the credentials path."""
        assert getattr(entrance, 'is_file')

    def test_credentials(self):
        """Test the credentials."""
        assert pkg.get_credentials(self.credentials_file)

    def test_email_class(self):
        """Test the email class."""
        expected = {
            'username': 'dev@example.com',
            'password': 'xpto',
            'hostname': 'imap.google.com',
        }
        assert (
            pkg.asdict(pkg.Email(**pkg.get_credentials(self.credentials_file)))
            == expected
        )
