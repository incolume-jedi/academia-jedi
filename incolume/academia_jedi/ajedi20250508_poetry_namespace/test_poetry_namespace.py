"""UnitTest for the namespace."""

import incolume.academia_jedi.ajedi20250508_poetry_namespace as pkg


class TestNamespace:
    """Test the namespace."""

    def test_namespace(self) -> None:
        """UnitTest the namespace."""
        assert (
            pkg.__name__
            == 'incolume.academia_jedi.ajedi20250508_poetry_namespace'
        )

    def test_namespace_cowsay(self) -> None:
        """UnitTest the namespace."""
        assert pkg.cow('Hello from ajedi20250508_poetry_namespace!') == (
            '  _______\n'
            '< Hello from ajedi20250508_poetry_namespace! >\n'
            '  -------\n'
            '         \\   ^__^\n'
            '          \\  (oo)\\_______\n'
            '             (__)\\       )\\/\\\n'
            '                 ||----w |\n'
            '                 ||     ||\n'
        )
