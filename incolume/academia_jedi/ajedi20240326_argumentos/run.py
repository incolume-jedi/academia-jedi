"""Argumento python."""


def f(a: int, b: int = 0, c: int = 0, d: int = 0):
    """Funct."""
    return a, b, c, d



def g(a: int, /, b: int = 0, c: int = 0, d: int = 0):
    """Funct."""
    return a, b, c, d

def h(a: int = 0, /, b: int = 0, *, c: int = 0, d: int = 0):
    """Funct."""
    return a, b, c, d

def i(*args, **kwargs):
    """Funct."""
    return {'args': args, **kwargs}

def j(a: int, /, *args, **kwargs):
    """Funct."""
    return {'args': args, **kwargs}


def run():
    """Run it."""
    print(
        f(1),
        f(1,2,3,4),
        f(a=1,d=2,b=3,c=4),
        g(1),
        g(1, 2, 3, 4),
        g(1, b=2, c=3, d=4),
        h(),
        h(1),
        h(1, b=2, c=3, d=4),
        h(1, 2, c=3, d=4),
        h(1, 2, d=4, c=3),
        i(1,2,3,4),
        i(2,1,4,3),
        i(b=2,a=1,d=4,c=3),
        j(1, b=2,d=4,c=3),
        sep='\n'
    )


if __name__ == '__main__':
    run()
