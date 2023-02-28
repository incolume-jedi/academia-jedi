import typing


def run():
    """Running it."""
    functions: typing.List[typing.Callable] = [
        value for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print('    >>> {}'.format(func.__doc__))
        try:
            if result := func():
                print(result)
        except ValueError as e:
            logging.error(f'{e.__class__.__name__}: {e}')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
