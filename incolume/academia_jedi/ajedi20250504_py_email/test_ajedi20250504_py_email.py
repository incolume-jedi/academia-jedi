"""Email with python."""

import inspect
import json
from pathlib import Path
import shutil
from tempfile import gettempdir
from typing import ClassVar

import pytest
import incolume.academia_jedi.ajedi20250504_py_email as pkg


class TestPyEmail:
    """Test the ajedi20250504_py_email package.

    This class contains test methods for the ajedi20250504_py_email package.
    """

    path_class: Path = Path(
        gettempdir(),
        inspect.stack()[0][3],
    )
    credentials_file: Path = path_class / 'credentials/credentials.json'
    credentials: ClassVar[dict[str, str]] = {
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
        """Test the import of the ajedi20250504_py_email package."""
        assert pkg.__name__ == 'incolume.academia_jedi.ajedi20250504_py_email'

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                {
                    'assunto': 'Test Email 1',
                    'destinatarios': ['jesoxid995@benznoi.com'],
                    'credentials_file': None,
                },
                True,
                marks=[pytest.mark.xfail()],
            ),
            pytest.param(
                {
                    'assunto': 'Second test send email',
                    'destinatarios': ['jesoxid995@benznoi.com'],
                    'credentials_file': credentials_file,
                },
                {
                    'expected_exception': pkg.smtplib.SMTPAuthenticationError,
                    'match': 'Username and Password not'
                    ' accepted. For more information',
                },
            ),
            pytest.param(
                {
                    'assunto': 'Test Email com anexo png',
                    'destinatarios': ['jesoxid995@benznoi.com'],
                    'credentials_file': None,
                    'subtype': 'html',
                    'template_conteudo': Path(__file__).parent.joinpath(
                        'content_html.txt',
                    ),
                    'sign': '<br><br><p><b>Ricardo Brito do Nascimento</b>'
                    '<br>Analista de Sistemas<br>'
                    'Junda Especializada de Desenvolvimento e Inovação<br>'
                    'Desenvolvimento Incolume</p>',
                    'anexo_path': Path(__file__)
                    .parents[3]
                    .joinpath('data_files', 'png', 'Logo_incolume.png'),
                },
                True,
                marks=[pytest.mark.xfail()],
            ),
            pytest.param(
                {
                    'assunto': 'Test Email com anexo svg',
                    'destinatarios': ['jesoxid995@benznoi.com'],
                    'credentials_file': None,
                    'subtype': 'html',
                    'template_conteudo': Path(__file__).parent.joinpath(
                        'content_html.txt',
                    ),
                    'sign': '<br><br><p><b>Ricardo Brito do Nascimento</b>'
                    '<br>Analista de Sistemas<br>'
                    'Junda Especializada de Desenvolvimento e Inovação<br>'
                    'Desenvolvimento Incolume</p>',
                    'anexo_path': Path(__file__)
                    .parents[3]
                    .joinpath('data_files', 'svg', 'logo_incolume.svg'),
                },
                True,
                marks=[pytest.mark.xfail()],
            ),
        ],
    )
    def test_send_email(self, entrance, expected):
        """Unitest for send_email function."""
        if isinstance(expected, dict) and 'expected_exception' in expected:
            with pytest.raises(**expected):
                pkg.send_email(**entrance)
        else:
            # Call the function with the credentials file and other parameters
            result = pkg.send_email(**entrance)
            assert result is expected
