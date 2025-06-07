"""Test suite for the ajedi20250604-secrets-dynaconf package."""

from __future__ import annotations
import ajedi20250604_secrets_dynaconf as pkg
from pathlib import Path
from tempfile import gettempdir
from icecream import ic
from dynaconf import Dynaconf
import pytest
import shutil

class TestAjedi20250604SecretsDynaconf:
    """Test suite for ajedi20250604-secrets-dynaconf."""

    output_dir: Path = Path(gettempdir()) / 'ajedi20250604_secrets_dynaconf'

    @classmethod
    def setup_class(cls):
        """Setup class."""
        ic(f'starting class {cls.__name__} execution')
        cls.output_dir.mkdir(parents=True, exist_ok=True)
        secret = cls.output_dir.joinpath('secrets.yml')
        secret.write_text(
            pkg.content,
            encoding='utf-8',
        )
        cls.settings = Dynaconf(
            environment=True,

            settings_files=[secret],
            environments=[
                'default',
                'development',
                'production',
                'testing',
            ],
        )

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        ic(f'finishing class {cls.__name__} execution')
        shutil.rmtree(cls.output_dir, ignore_errors=True)


    def test_package_import(self) -> None:
        """Test if the package can be imported successfully."""
        assert pkg is not None

    def test_package_load_yaml_config(self) -> None:
        """Test if the load_yaml_config function works correctly."""
        assert isinstance(pkg.load_yaml_from_str(content=pkg.content), dict)

    def test_dumps_yaml(self) -> None:
        """Test if the dumps_yaml function works correctly."""
        data = pkg.load_yaml_from_str(content=pkg.content)
        yaml_str = pkg.dumps_yaml(data)
        assert isinstance(yaml_str, str)
        assert (
            yaml_str.strip()
            == 'default:\n  password: 123@pwd\ndevelopment: null\n'
            'production:\n'
            '  password: sek@987342$\ntesting:\n  password: 777777'
        )

    def test_dumps_toml(self) -> None:
        """Test if the dumps_toml function works correctly."""
        data = pkg.load_yaml_from_str(content=pkg.content)
        toml_str = pkg.dumps_toml(data)
        assert isinstance(toml_str, str)
        assert (
            toml_str.strip()
            == '[default]\npassword = "123@pwd"\n\n[production]\npassword'
            ' = "sek@987342$"\n\n[testing]\npassword = 777777'
        )

    def test_dumps_json(self) -> None:
        """Test if the dumps_json function works correctly."""
        data = pkg.load_yaml_from_str(content=pkg.content)
        json_str = pkg.dumps_json(data)
        assert isinstance(json_str, str)
        assert (
            json_str.strip()
            == '{\n  "default": {\n    "password": "123@pwd"\n  },\n  '
            '"development": null,\n  "production": {\n    '
            '"password": "sek@987342$"\n  },\n  '
            '"testing": {\n    "password": 777777\n  }\n}'
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('production', 'sek@987342$'),
            ('development', '123@pwd'),
            ('testing', '777777a'),
            (None, '123@pwd'),
        ],
    )
    def test_settings(self, entrance, expected) -> None:
        """Test if the settings are loaded correctly."""
        assert self.settings.from_env(entrance).password == expected
