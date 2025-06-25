"""Mescla de planilhas."""

import inspect
from pathlib import Path
from tempfile import gettempdir

import pandas as pd
from icecream import ic

path: Path = Path(__file__).parents[3].joinpath('data_files', 'csv')


def show_files_dir(directory: Path) -> None:
    """Show files."""
    for file in directory.iterdir():
        print(ic(file))


def merge_planilhas(directory: Path, fout: None | Path = None) -> Path:
    """Merge planilhas."""
    fout = fout or Path(
        gettempdir(),
        (f := inspect.stack()[0][3]),
        f'{f.casefold()}.csv',
    )
    df0 = pd.DataFrame()
    for file in directory.rglob('supermarket*_?.csv'):
        ic(file)
        df_temp = pd.read_csv(file)
        df0 = pd.concat([df0, df_temp])
    df0.sort_values(['City', 'Invoice ID']).to_csv(fout, index=False, sep=';')
    return fout
