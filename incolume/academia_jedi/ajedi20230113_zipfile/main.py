import logging
from pathlib import Path
import shutil
import realpython01
import realpython02
import realpython03
import realpython04
import realpython05
import realpython06
import realpython07
import realpython08
import realpython09
import realpython10
import realpython11
import realpython12
import realpython13
import realpython14
import realpython15
import realpython16
import realpython17
import realpython18
import realpython19
import realpython20
import realpython21
import realpython22
import realpython23
import realpython24
import realpython25
import realpython26
import realpython27
import realpython28
import realpython29
import realpython30
import realpython31
import realpython32
import realpython33

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
