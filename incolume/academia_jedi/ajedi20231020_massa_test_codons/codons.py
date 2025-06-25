"""Criar cadeias de códons para massa de testes."""

# ruff: noqa: B007, PLR2004, S311

import random
from typing import Final


def massa_codon_dna0(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    alfabeto: Final = 'ACGT'
    tamanho_codon = min(tamanho_codon, 1000)
    tamanho_codon = max(4, tamanho_codon)
    codon = random.choices(alfabeto, k=tamanho_codon)
    return ''.join(codon)


def massa_codon_dna1(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    alfabeto = 'ACGT'
    if tamanho_codon > 1000:
        return 'Tamanho superior ao limite de 1000'
    if tamanho_codon < 4:
        return 'Tamanho inferior ao limite de 4'
    codon = random.choices(alfabeto, k=tamanho_codon)
    return ''.join(codon)


def massa_codon_dna(tamanho_codon: int = 4) -> str:
    """Verificar se codon está no alfabeto do DNA."""
    alfabeto = 'ACGT'
    if tamanho_codon > 1000:
        msg = 'Tamanho superior ao limite de 1000'
        raise ValueError(msg)
    if tamanho_codon <= 4:
        msg = 'Tamanho inferior ao limite de 4'
        raise ValueError(msg)
    codon = random.choices(alfabeto, k=tamanho_codon)
    return ''.join(codon)


if __name__ == '__main__':  # pragma: no cover
    for i in range(10):
        print(massa_codon_dna(random.randint(2, 1001)))
