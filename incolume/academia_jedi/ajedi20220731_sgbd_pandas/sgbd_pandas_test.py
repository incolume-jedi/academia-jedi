from incolume.academia_jedi.ajedi20220731_sgbd_pandas.main import massa_test


class CheckSGBDPandas:
    """Test de demandas."""

    def test_massa(self):
        """Test it."""
        assert isinstance(massa_test(), list)

    def test_example01(self):
        """Test example01."""
