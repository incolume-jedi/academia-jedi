"""Test for this module."""

import incolume.academia_jedi.ajedi20250204 as pkg


class TestCase:
    """Test case."""

    def test_0(self):
        """Unit test."""
        assert set('academia_jedi ajedi20250204'.split()).issubset(
            pkg.directories.parts,
        )

    def test_1(self):
        """Unit test."""
        assert isinstance(pkg.list_dir(pkg.directories), map)
