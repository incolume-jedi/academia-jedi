from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument("square", help="squares a given number", type=int)
parser.add_argument(
    "-v", "--verbose", help="show details", type=int, choices=[0, 1, 2], default=0
)

args: Namespace = parser.parse_args()

result = args.square**2

if args.verbose == 0:
    print(result)
elif args.verbose == 1:
    print(f"{args.square} ** 2 = {result}")
elif args.verbose == 2:
    print(f"{args.square} ao quadrado é: {result}")
