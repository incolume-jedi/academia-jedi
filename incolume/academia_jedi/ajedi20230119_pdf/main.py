import tratativa1
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


def run():
    tratativa1.ex01()



if __name__ == '__main__':
    run()
