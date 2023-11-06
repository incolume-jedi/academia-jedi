import logging
import shutil
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)
root = Path(__file__).parent
logging.debug(root)


def clean_workdir():
    """Remover arquivos gerados após execução."""
    all_files = set(root.rglob('*'))
    logging.debug(all_files)

    truth_files = (
        list(root.rglob('*.py'))
        + list(root.rglob('sample*'))
        + list(root.rglob('python-zipfile*'))
        + list(root.rglob('.git*'))
    )
    logging.debug(f'{truth_files=}')

    wanted_files = all_files.difference(truth_files)
    logging.debug(f'{wanted_files=}')
    [file.unlink(missing_ok=True) for file in wanted_files if file.is_file()]
    [shutil.rmtree(file) for file in wanted_files if file.is_dir()]


def run():
    functions = [
        getattr(eval(f'realpython{x:02}'), 'run') for x in range(1, 34)
    ]
    for func in functions:
        logging.debug(func.__name__)
        try:
            func()
        except (FileNotFoundError, ImportError) as e:
            logging.error(e)
    clean_workdir()


if __name__ == '__main__':
    run()
