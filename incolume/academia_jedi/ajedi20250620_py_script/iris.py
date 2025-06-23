#!/usr/bin/env python3
"""Script iris."""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click>=8.1.8",
#     "pandas==2.2.3",
#     "ucimlrepo>=0.0.7",
# ]
# ///

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum, auto
from pprint import pformat
from pprint import pprint as pp

import click
import pandas as pd
from icecream import ic
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

    @classmethod
    def _missing_(cls, value):
        """Get item."""
        value = str(value).casefold()
        for member in cls:
            if member.value == value or member.name == value.upper().replace(
                ' ',
                '_',
            ):
                return member
        return None

    @classmethod
    def options(cls):
        """Options."""
        result = [x.name for x in cls]
        result.extend(x.value for x in cls)
        return result


class Operation(StrEnum):
    SUMMARY = auto()
    METADATA = auto()


@dataclass
class DescriptiveStatistics:
    data: pd.Series
    mean: float = field(init=False)
    median: float = field(init=False)
    mm_diff: float = field(init=False)

    def __post_init__(self):
        if not isinstance(self.data, pd.Series):
            raise TypeError(
                f'data must be a pandas Series, not {type(self.data)}',
            )
        self.mean = self.data.mean()
        self.median = self.data.median()
        self.mm_diff = self.mean - self.median

    def __str__(self):
        return pformat(self)


@click.command()
@click.option(
    '--operation',
    '-o',
    default=Operation.SUMMARY,
    type=click.Choice(Operation, case_sensitive=False),
    help='Operation to perform: variable summary or dataset metadata',
)
@click.option(
    '--variable',
    '-v',
    type=click.Choice(IrisVariable.options(), case_sensitive=False),
    help='Variable to summarize.',
    required=False,
)
def main(operation: str, variable: str) -> None:
    """Chamada script iris."""
    print('Hello from script iris.py!')
    print('Fetching Iris dataset using ucimlrepo...')
    iris = fetch_ucirepo(id=UCIDataset.IRIS.value)
    print('Dataset fetched successfully.')

    match operation:
        case Operation.SUMMARY:
            if variable:
                print(f'{IrisVariable(variable)} summary:')
                print(
                    DescriptiveStatistics(
                        iris.data.features[IrisVariable(variable).value],
                    ),
                )
            else:
                print('All variables:')
                pp(iris.variables)
        case Operation.METADATA:
            print('Metadata summary:')
            pp(iris.metadata)


if __name__ == '__main__':
    ic(IrisVariable.PETAL_LENGTH)
    ic(IrisVariable('petal_length'))
    ic(IrisVariable('petal length'))
    ic({x.name: x.value for x in IrisVariable})
    main()
