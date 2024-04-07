"""Should you use "not not x" instead of "bool(x)" in Python? (NO!)."""
import logging
import timeit
import typing


def bool_convert(x):
    return bool(x)


def notnot_convert(x):
    return bool(x)


def dundler_bool_convert(x):
    """"""
    return x.__bool__()


def tratativa1():
    """Compare boolean conveters."""
    trails = 10_000_000
    kwargs = {'setup': 'x=42', 'globals': globals(), 'number': trails}

    notnot_time = timeit.timeit('notnot_convert(x)', **kwargs)
    bool_time = timeit.timeit('bool_convert(x)', **kwargs)
    dundler_bool_time = timeit.timeit('dundler_bool_convert(x)', **kwargs)

    print(f'{bool_time=:.02f}')
    print(f'{notnot_time=:.02f}')
    print(f'{dundler_bool_time=:.02f}')


def run():
    """Running it."""
    functions: list[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print(f'    >>> {func.__doc__}')
        try:
            if result := func():
                print(result)
        except (TypeError, ValueError) as e:
            logging.exception(f'{e.__class__.__name__}: {e}')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
