"""Estudos sobre desempacotamento em variáveis."""


def ex1():
    """Exemplo 1."""
    x = (1, 2, 3)
    a, b, c = x
    print(f'{a=} {b=} {c=}')  # noqa: T201


def func(a, b, c):
    """Func for printing."""
    print(f'{a=} {b=} {c=}')  # noqa: T201


def ex2():
    """Exemplo 1."""
    x = (1, 2, 3)
    func(*x)


def ex3():
    """Exemplo 1."""
    x = {'1': 1, '2': 2, '3': 3}
    func(*x.values())


def ex4():
    """Exemplo 1."""
    x = {'a': 1, 'b': 2, 'c': 3}
    func(*x.keys())


def ex5():
    """Exemplo 1."""
    x = {'a': 1, 'b': 2, 'c': 3}
    func(**x)


def run():
    """Run it."""
    ex5()


if __name__ == '__main__':
    run()
