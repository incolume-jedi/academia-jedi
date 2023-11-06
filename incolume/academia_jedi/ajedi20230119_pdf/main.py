import logging

import tratativa1
import tratativa2

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    tratativa1.ex01()
    tratativa1.ex02()
    tratativa1.ex03()
    tratativa1.ex04()
    tratativa2.ex01()
    tratativa2.ex02()
    tratativa2.ex03()


if __name__ == '__main__':
    run()
