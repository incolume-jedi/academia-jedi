#!/usr/bin/env python3
"""Script iris."""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click>=8.1.8",
#     "ucimlrepo>=0.0.7",
# ]
# ///

from enum import IntEnum, StrEnum
from pprint import pprint as pp

import click
from ucimlrepo import fetch_ucirepo


class UCIDataset(IntEnum):
    """class for UCIDataSet."""

    IRIS = 53


class IrisVariable(StrEnum):
    """class for IrisVariable."""

    PETAL_LENGTH = 'petal length'
    PETAL_WIDTH = 'petal width'
    SEPAL_WIDTH = 'sepal width'
    SEPAL_LENGTH = 'sepal length'


@click.command()
@click.option(
    '--operation',
    '-o',
    default='summary',
    type=click.Choice(['summary', 'metadata']),
    help='Operation to perform: variable summary or dataset metadata',
)
@click.option(
    '--variable',
    '-v',
    type=click.Choice(IrisVariable),
    help='Variable to summarize.',
    required=False,
)
def main(operation: str, variable: str) -> None:
    """Chamada script iris."""
    print('Hello from script iris.py!')
    print('Fetching Iris dataset using ucimlrepo...')
    iris = fetch_ucirepo(id=UCIDataset.IRIS.value)
    print('Dataset fetched successfully. Variable summary:')
    print(iris.variables)

    if operation == 'summary':
        if variable:
            print(f'{IrisVariable(variable)} summary:')
            pp(iris.data.features[IrisVariable(variable).value])
        else:
            print('All variables:')
            pp(iris.variables)
    elif operation == 'metadata':
        print('Metadata summary:')
        pp(iris.metadata)


if __name__ == '__main__':
    main()
