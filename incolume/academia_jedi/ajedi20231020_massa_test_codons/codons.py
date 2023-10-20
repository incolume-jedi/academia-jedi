import random


def massa_codon_dna0(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    ALFABETO = 'ACGT'
    if tamanho_codon > 1000:
        tamanho_codon = 1000
    if tamanho_codon <= 4:
        tamanho_codon = 4
    codon = random.choices(ALFABETO, k = tamanho_codon)
    return ''.join(codon)


def massa_codon_dna1(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    ALFABETO = 'ACGT'
    if tamanho_codon > 1000:
        return 'Tamanho superior ao limite de 1000'
    if tamanho_codon < 4:
        return 'Tamanho inferior ao limite de 4'
    codon = random.choices(ALFABETO, k = tamanho_codon)
    return ''.join(codon)


def massa_codon_dna(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    ALFABETO = 'ACGT'
    if tamanho_codon > 1000:
        raise ValueError('Tamanho superior ao limite de 1000')
    if tamanho_codon <= 4:
        raise ValueError('Tamanho inferior ao limite de 4')
    codon = random.choices(ALFABETO, k = tamanho_codon)
    return ''.join(codon)