"""Main Module."""
<<<<<<< HEAD

import logging

import exemplo1
import exemplo2

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
=======
import logging
import exemplo1
import exemplo2
import exemplo3

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
>>>>>>> 848249a (feat: Operador morsa atualizado)
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    exemplo1.run()
    exemplo2.run()


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> 848249a (feat: Operador morsa atualizado)
    run()
