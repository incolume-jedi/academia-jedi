"""zen do python."""
import logging

__author__ = '@britodfbr'  # pragma: no cover
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """"""
    logging.debug(globals())
    items = (value for key, value in globals().items() if key.startswith('ex'))

    for item in items:
        print(f'--- {item.__name__} ---')
        try:
            print(item.run())
        except AttributeError as e:
            logging.error(f'{e.__class__.__name__}:{e}')
        print()


if __name__ == '__main__':  # pragma: no cover
    run()
