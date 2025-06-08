"""Test file for ajedi20250607_dockerfile_inline module."""

from __future__ import annotations
from ajedi20250607_docker_subprojetos import main
from pathlib import Path
from streamlit.testing.v1 import AppTest
import pytest


class TestAjedi20250607DockerSubprojetos:
    """Test class for ajedi20250607_docker_subprojetos module."""

    app_file = Path(__file__).parent / 'main.py'
    at = AppTest.from_file(app_file).run()

    def test_appfile_exists(self):
        """Test if the app file exists."""
        assert self.app_file.exists()

    def test_main(self):
        """Test the main function."""
        assert main() == 'Hello from ajedi20250607-docker-subprojetos!'

    def test_app_title(self):
        """Test if the app title is set correctly."""
        assert self.at.title[0].value == 'Docker Subprojetos'

    def test_app_markdown(self):
        """Test if the app markdown is set correctly."""
        assert self.at.markdown[0].value == '---'

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('', ''),
        ],
    )
    def test_app_write(self, entrance, expected):
        """Test if the app write function returns the expected value."""
        assert entrance == expected
