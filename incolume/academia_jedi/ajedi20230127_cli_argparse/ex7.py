from argparse import ArgumentParser, Namespace
import logging


parser = ArgumentParser()

# parser.usage = 'Use it like this'
parser.add_argument('a', help='base value', type=int, default=1, nargs='?')
parser.add_argument(
    'b', help='expoent value', type=float, default=1, nargs='?'
)
parser.add_argument(
    '-v', '--verbose', help='show details (-v| -vv| -vvv)', action='count'
)

args: Namespace = parser.parse_args()

result: int = args.a**args.b

logging.debug(args.verbose)

match args.verbose:
    case None:
        print(result)
    case 1:
        print('resultado:', result)
    case 2:
        print(f'{args.a} ** {args.b} = {result}')
    case _:
        print(f'{args.a} elevado a {args.b} é: {result}')
