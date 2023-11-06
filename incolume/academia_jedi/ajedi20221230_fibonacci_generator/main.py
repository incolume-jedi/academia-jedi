from truncus import fibonacci0, fibonacci1, fibonacci2

__author__ = '@britodfbr'  # pragma: no cover


if __name__ == '__main__':  # pragma: no cover
    fib = fibonacci0()
    for i in range(1, 11):
        print(i, next(fib))
    print(next(fib))

    for i in fibonacci1(10):
        print(i)
    print(list(fibonacci1(11)))

    for j in fibonacci2(5):
        print(j)
