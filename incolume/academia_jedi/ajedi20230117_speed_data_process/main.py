import pandas as pd

from fake_data import get_dataset, set_dtypes
from pathlib import Path
import logging
from time import perf_counter
from timeit import timeit
from tempfile import gettempdir


__author__ = '@britodfbr'  # pragma: no cover
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

file = Path(gettempdir()) / 'file.txt'


def write(df: pd.DataFrame, file: Path, suffix: str = 'csv') -> bool:
    """Write databases."""
    suffix = suffix if suffix.startswith('.') else f'.{suffix}'
    rfunctions = {
        '.csv': df.read_csv,
        '.json': df.read_json,
    }
    wfunctions = {
        '.csv': df.to_csv,
        '.json': df.to_json,
    }
    logging.debug(suffix.upper())
    it = perf_counter()
    wfunctions.get(suffix)(f := file.with_suffix(f'.{suffix}'), index=False)
    it = perf_counter() - it
    ft = perf_counter()
    rfunctions.get(suffix)(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )
    return True


def run():
    df = set_dtypes(get_dataset(1_000_000))
    print(df)
    print(df.info())

    # CSV
    it = perf_counter()
    df.to_csv(f := file.with_suffix('.csv'), index=False)
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_csv(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )

    # JSON
    it = perf_counter()
    df.to_json(f := file.with_suffix('.json'), orient='records', indent=2)
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_json(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )

    # XLSX
    it = perf_counter()
    df.to_excel(f := file.with_suffix('.xlsx'), index=False)
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_excel(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )

    # Pickle
    it = perf_counter()
    df.to_pickle(f := file.with_suffix('.pkl'))
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_pickle(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )

    # Parquet
    it = perf_counter()
    df.to_parquet(f := file.with_suffix('.parquet'))
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_parquet(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )

    # Feather
    it = perf_counter()
    df.to_feather(f := file.with_suffix('.feather'))
    it = perf_counter() - it
    ft = perf_counter()
    df = pd.read_feather(f)
    ft = perf_counter() - ft
    logging.debug(
        '{:15}: {:15}; time w:{}; time r: {}'.format(
            f.as_posix(), f.stat().st_size, it, ft
        )
    )


if __name__ == '__main__':  # pragma: no cover
    run()
    """
    2023-01-17 23:36:54,559;DEBUG   ;root;main;run;/tmp/file.csv  :        37205166; time w:1.8565981949977868; time r: 0.2632749270014756
    2023-01-17 23:36:57,681;DEBUG   ;root;main;run;/tmp/file.json :       121205270; time w:0.7760083579996717; time r: 2.346326267001132
    2023-01-17 23:40:04,558;DEBUG   ;root;main;run;/tmp/file.xlsx :        31529731; time w:105.81597516600232; time r: 81.0606829540011
    2023-01-17 23:40:04,657;DEBUG   ;root;main;run;/tmp/file.pkl  :        29005868; time w:0.07388097500006552; time r: 0.025677702000393765
    2023-01-17 23:40:05,013;DEBUG   ;root;main;run;/tmp/file.parquet:         4591312; time w:0.3044267210025282; time r: 0.050775613002770115
    2023-01-17 23:40:05,128;DEBUG   ;root;main;run;/tmp/file.feather:        22183146; time w:0.07782294400021783; time r: 0.03724654100005864
"""
