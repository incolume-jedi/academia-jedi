from incolume.academia_jedi.ajedi20231020_complementar_fita_dna.dojo import complemento_fita_dna, complemento_codon, complement_codon
import pytest


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('AAAACCCGGT', 'ACCGGGTTTT'),
    ],
)
def test_complemento_fita_dna(entrance, expected) -> None:
    """Testar a função complemento_fita_dna."""
    assert complemento_fita_dna(entrance) == expected
    

@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('AAAACCCGGT', 'ACCGGGTTTT'),
    ],
)
def test_complemento_codon(entrance, expected) -> None:
    """Testar a função complemento_fita_dna."""
    assert complemento_codon(entrance) == expected
    

@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('AAAACCCGGT', 'ACCGGGTTTT'),
    ],
)
def test_complement_codon(entrance, expected) -> None:
    """Testar a função complemento_fita_dna."""
    assert complement_codon(entrance) == expected