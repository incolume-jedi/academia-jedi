"""Dojo contagem de nucleotídeos."""


def contador_nucleotideos(nucleotideo: str) -> str:
    """Contar nucleotídeos."""
    a, c, g, t = 0, 0, 0, 0

    for codigo in nucleotideo:
        if codigo == 'A':
            a += 1
        elif codigo == 'C':
            c += 1
        elif codigo == 'G':
            g += 1
        elif codigo == 'T':
            t += 1

    return str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)


def cont_nucleotideos(codon: str) -> str:
    """Contar nucleotídeos."""
    return f"{codon.count('A')} {codon.count('C')} {codon.count('G')} {codon.count('T')}"
