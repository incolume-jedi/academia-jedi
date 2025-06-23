#!/usr/bin/env python3
"""Script iris."""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click>=8.1.8",
#     "ucimlrepo>=0.0.7",
# ]
# ///

from pprint import pprint as pp

import click
from ucimlrepo import fetch_ucirepo

IRIS_DATASET_ID = 53


@click.command()
@click.option(
    '--operation',
    '-o',
    default='summary',
    type=click.Choice(['summary', 'metadata']),
    help='Operation to perform: variable summary or dataset metadata',
)
def main(operation: str) -> None:
    """Chamada script iris."""
    print('Hello from script iris.py!')
    print('Fetching Iris dataset using ucimlrepo...')
    iris = fetch_ucirepo(id=IRIS_DATASET_ID)
    print('Dataset fetched successfully. Variable summary:')
    print(iris.variables)

    if operation == 'summary':
        print('Variable summary:')
        pp(iris.variables)
    elif operation == 'metadata':
        print('Metadata summary:')
        pp(iris.metadata)


if __name__ == '__main__':
    main()
