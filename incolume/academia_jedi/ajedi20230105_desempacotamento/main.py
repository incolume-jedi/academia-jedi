def ex1():

    x = (1, 2, 3)
    a, b, c = x
    print(f"{a=} {b=} {c=}")


def func(a, b, c):
    print(f"{a=} {b=} {c=}")


def ex2():
    x = (1, 2, 3)
    func(*x)


def ex3():
    x = {"1": 1, "2": 2, "3": 3}
    func(*x.values())


def ex4():
    x = {"a": 1, "b": 2, "c": 3}
    func(*x.keys())


def ex5():
    x = {"a": 1, "b": 2, "c": 3}
    func(**x)


def run():
    ex5()


if __name__ == "__main__":
    run()
