"""Testes Unitarios."""

import incolume.academia_jedi.ajedi20250414_estudos_streamlit as pkg


def test_datafile():
    """Unittest."""
    assert pkg.datafile.is_file()
