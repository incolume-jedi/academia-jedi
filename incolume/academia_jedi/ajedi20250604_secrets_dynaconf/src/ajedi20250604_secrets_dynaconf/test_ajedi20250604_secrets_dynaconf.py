"""Test suite for the ajedi20250604-secrets-dynaconf package."""

from __future__ import annotations
import ajedi20250604_secrets_dynaconf as pkg


class TestAjedi20250604SecretsDynaconf:
    """Test suite for ajedi20250604-secrets-dynaconf."""

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
