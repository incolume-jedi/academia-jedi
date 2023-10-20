def complemento_fita_dna(fita: str) -> str:
    """Complementar fita."""
    sc = ''
    for s in fita.upper()[::-1]:
        if s == 'A':
            sc += 'T'
        if s == 'T':
            sc += 'A'
        if s == 'G':
            sc += 'C'
        if s == 'C':
            sc += 'G'
    return sc


def complemento_codon(fita: str) -> str:
    """Complementar fita."""
    codon = {
        'A': 'T', 
        'T': 'A', 
        'C': 'G', 
        'G': 'C',
        }
    sc = ''
    for s in fita.upper()[::-1]:
        sc += codon[s]
    return sc


def complement_codon(fita: str) -> str:
    """Complementar fita."""
    codon = {
        'A': 'T', 
        'T': 'A', 
        'C': 'G', 
        'G': 'C',
        }
    return ''.join(codon[s] for s in fita.upper()[::-1])