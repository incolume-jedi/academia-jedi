import logging
import random
import string

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


class BadFormationError(ValueError):
    pass


def generate_random_str(length: int = 8) -> str:
    length = length if length > 8 else 8
    chars: str = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def fuzzer() -> str:
    while True:
        yield generate_random_str(random.randint(1, 100))


def sample_func(input_str: str) -> int:
    try:
        if '!!!' in input_str:
            msg = 'Bad formation'
            raise BadFormationError(msg)
        return 0
    except Exception as e:
        logging.error('%s: %s', e.__class__.__name__, e)
        return 1


def main():
    for i, input_str in enumerate(fuzzer()):
        result: int = sample_func(input_str)

        if result != 0:
            logging.error(f'Ran #{i}: {input_str}')
            break


def run():
    logging.debug(generate_random_str())
    main()


if __name__ == '__main__':  # pragma: no cover
    run()
