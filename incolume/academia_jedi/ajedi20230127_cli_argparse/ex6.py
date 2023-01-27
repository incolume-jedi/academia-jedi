from argparse import ArgumentParser, Namespace
import logging


parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int, default=0, nargs='?')
parser.add_argument('-v', '--verbose', help='show details', action='count' )

args: Namespace = parser.parse_args()

result = args.square ** 2

logging.debug(args.verbose)

if not args.verbose:
    print(result)
elif args.verbose == 1:
    print(f'{args.square} ** 2 = {result}')
elif args.verbose >= 2:
    print(f'{args.square} ao quadrado é: {result}')