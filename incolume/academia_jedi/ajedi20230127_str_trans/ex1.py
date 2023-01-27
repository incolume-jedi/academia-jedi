from tratativa1 import elements_this
import logging


def run():
    entrance, cipher, _ = elements_this()

    # result = entrance[:]

    decoder = str.maketrans(cipher)
    logging.debug(decoder)
    
    result = entrance.translate(decoder)

    return result


if __name__ == "__main__":
    print(run())
