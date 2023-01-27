from argparse import ArgumentParser, Namespace
import logging


def run():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    # parser.usage = 'Use it like this'

    parser.add_argument('a', help='base value', type=int, default=1, nargs='?')
    parser.add_argument('b', help='expoent value', type=float, default=1, nargs='?')
    group.add_argument('-v', '--verbose', help='show details (-v| -vv| -vvv)', action='count' )
    group.add_argument('-s', '--silence', help='silence mode', action='store_true' )

    args: Namespace = parser.parse_args()

    result: int = args.a ** args.b

    logging.debug(args.verbose)
    if args.silence:
        return

    match args.verbose:
        case None: 
            print(result)
        case 1:
            print('resultado:', result)
        case 2:
            print(f'{args.a} ** {args.b} = {result}')
        case _:
            print(f'{args.a} elevado a {args.b} é: {result}')


if __name__ == '__main__':
    run()
