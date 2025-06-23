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
import logging
import sys
import click
import pandas as pd
from icecream import ic
from ucimlrepo import fetch_ucirepo


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
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

    iris = fetch_iris()

    match operation:
        case Operation.SUMMARY:
            if variable:
                logging.info(f'{IrisVariable(variable)} summary:')
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
    logging.info("Fetching Iris dataset...")
    try:
        iris_data = fetch_ucirepo(id=UCIDataset.IRIS.value)
    except Exception as e:
        logging.critical(f"Failed to correctly fetch Iris dataset: {e}")
        sys.exit(1)
    else:
        logging.info("Iris dataset fetched successfully")
        return iris_data


if __name__ == '__main__':
    ic(IrisVariable.PETAL_LENGTH)
    ic(IrisVariable('petal_length'))
    ic(IrisVariable('petal length'))
    ic({x.name: x.value for x in IrisVariable})
    main()
