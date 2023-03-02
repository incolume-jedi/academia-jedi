"""Main Module."""
import logging
import exemplo1
import exemplo2
import exemplo3
import exemplo4
import exemplo5
import exemplo6
import exemplo7
import exemplo8
import exemplo9
import exemplo10
import exemplo11
import exemplo12
import exemplo13


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def run():
    """Run main module."""
    logging.debug("starting ..")
    exemplo1.run()
    exemplo2.run()
    exemplo3.run()
    exemplo4.run()
    exemplo5.run()
    exemplo6.run()
    exemplo7.run()
    exemplo8.run()
    exemplo9.run()
    exemplo10.run()
    exemplo11.run()
    exemplo12.run()
    exemplo13.run()


if __name__ == "__main__":
    run()
