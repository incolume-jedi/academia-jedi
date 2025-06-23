#!/usr/bin/env python3
"""Script iris."""

# ruff: noqa: EXE001 S101 BLE001

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click>=8.1.8",
#     "pandas==2.2.3",
#     "rich==14.0.0",
#     "ucimlrepo>=0.0.7",
# ]
# ///

import logging
import sys
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum, auto
from pprint import pformat

import click
import pandas as pd
from rich.console import Console, Text
from rich.logging import RichHandler
from rich.table import Table
from ucimlrepo import fetch_ucirepo

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s;%(name)s;%(levelname)-8s;%(module)s;%(funcName)s;%(message)s',
    handlers=[RichHandler(rich_tracebacks=True)],
)

logging.info('Hello from script iris.py!')


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
    """Operation class."""

    SUMMARY = auto()
    METADATA = auto()


@dataclass
class DescriptiveStatistics:
    """DescriptiveStatistics class."""

    data: pd.Series
    mean: float = field(init=False)
    median: float = field(init=False)
    mm_diff: float = field(init=False)

    def __post_init__(self):
        """Post init.

        Raises:
            TypeError: for wrong data.
        """
        if not isinstance(self.data, pd.Series):
            msg = 'data must be a pandas Series, not %s', type(self.data)
            raise TypeError(msg)
        self.mean = self.data.mean()
        self.median = self.data.median()
        self.mm_diff = self.mean - self.median

    def __str__(self):
        """To string."""
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
    console = Console()
    logging.debug(console)

    iris = fetch_iris()

    match operation:
        case Operation.SUMMARY:
            if variable:
                table = generate_table(iris, variable)
                logging.info(format_rich_for_log(table))
                logging.info('%s summary:', IrisVariable(variable))
                logging.info(
                    DescriptiveStatistics(
                        iris.data.features[IrisVariable(variable).value],
                    ),
                )
            else:
                logging.info('All variables:')
                logging.info(pformat(iris.variables))
        case Operation.METADATA:
            logging.info('Metadata summary:')
            logging.info(pformat(iris.metadata))


def fetch_iris():
    """Return the Iris dataset from the UCI ML Repository."""
    logging.info('Fetching Iris dataset...')
    try:
        iris_data = fetch_ucirepo(id=UCIDataset.IRIS.value)
        assert 'data' in iris_data, 'Object does not have expected structure'
    except Exception as e:
        logging.critical('Failed to correctly fetch Iris dataset: %s', e)
        sys.exit(1)
    else:
        logging.info('Iris dataset fetched successfully')
        return iris_data


def generate_table(dataset, variable):
    """Generate a formatted table of descriptive statistics for a variable."""
    column = IrisVariable(variable).value
    stats = DescriptiveStatistics(dataset.data.features[column])
    table = Table(title=f'{column} summary')
    table.add_column('Metric', style='cyan', justify='right')
    table.add_column('Value', style='magenta')
    table.add_row('Mean', f'{stats.mean:.2f}')
    table.add_row('Median', f'{stats.median:.2f}')
    table.add_row('Mean-Median Diff', f'{stats.mm_diff:.2f}')
    return table


def format_rich_for_log(renderable, width=80):
    """Render a rich object to a plain text string suitable for logging."""
    console = Console(width=width)
    with console.capture() as capture:
        console.print(renderable)
    return Text.from_ansi(capture.get())


if __name__ == '__main__':
    main()
