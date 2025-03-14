"""Test module."""

import incolume.academia_jedi.ajedi20221207_itertools_takewhile as pkg


def test_itertools_takewhile(capsys):
    """Unittest."""
    pkg.without_takewhile(pkg.numbers)
    output1 = capsys.readouterr()
    pkg.with_takewhile(pkg.numbers)
    output2 = capsys.readouterr()

    assert output1.out == output2.out
