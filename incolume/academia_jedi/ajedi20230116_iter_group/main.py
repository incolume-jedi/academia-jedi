from itertools import chain


__author__ = '@britodfbr'  # pragma: no cover


def tratativa1():
    matrix = [[x for x in range(3)] * 3]
    return matrix


def run():
    print(list(tratativa1()))


if __name__ == '__main__':  # pragma: no cover
    # print(help(chain))
    run()
