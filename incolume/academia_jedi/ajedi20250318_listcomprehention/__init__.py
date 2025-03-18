"""EStudo sobre listcomprehentions."""

# ruff: noqa: T201 PERF401
valores: list[int] = [30, 50, 100, 120]


def generate_triplo(entrada: list[int]) -> None:
    """Gerador de triplo.

    Sem listcomprehention.
    """
    triplos = []
    for valor in entrada:
        triplos.append(valor * 3)
    print(triplos)


def gen_multiple(entrance: list[int], fator: int = 3) -> None:
    """Gerador multiplos com listcomprehention."""
    fator = fator if fator > 1 else 2
    print([valor * fator for valor in entrance])
