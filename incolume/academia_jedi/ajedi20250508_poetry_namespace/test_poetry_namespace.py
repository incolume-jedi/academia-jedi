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
