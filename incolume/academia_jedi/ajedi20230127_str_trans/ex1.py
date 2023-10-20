import logging

from tratativa1 import elements_this


def tratativa1():
    entrance, cipher, _ = elements_this()
    logging.debug(entrance)
    # result = entrance[:]

    decoder = str.maketrans(cipher)
    logging.debug(decoder)

    result = entrance.translate(decoder)
    logging.debug(result)

    return result


if __name__ == '__main__':
    print(tratativa1())
