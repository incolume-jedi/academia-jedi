"""Module."""

import logging
import shutil
from pathlib import Path
from tempfile import gettempdir

from config import settings
from icecream import ic

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
    datefmt=settings.datefmt,
)


filezip_sample = (
    Path(__file__).parents[3].joinpath('data_files', 'zip', 'sample.zip')
)
logger.info(ic(filezip_sample))

filezip_sample_pwd = (
    Path(__file__).parents[3].joinpath('data_files', 'zip', 'sample_pwd.zip')
)
logger.info(ic(filezip_sample_pwd))

filezip_sample_pwd1 = (
    Path(__file__)
    .parents[3]
    .joinpath('data_files', 'zip', 'sample_file_pwd.zip')
)
logger.info(ic(filezip_sample_pwd1))

filezip_sample_pwd2 = (
    Path(__file__)
    .parents[3]
    .joinpath('data_files', 'zip', 'sample_file_pwd1.zip')
)
logger.info(ic(filezip_sample_pwd2))

base_dir = Path(gettempdir(), Path(__file__).parts[-2])
base_dir.mkdir(exist_ok=True, parents=True)
logger.info(ic(base_dir))

root = Path(__file__).parent
logger.info(ic(root))

outputdir = Path(__file__).parent / 'python-zipfile'
logger.info(ic('%s %s', outputdir, outputdir.exists()))


def clean_workdir():
    """Remover arquivos gerados após execução."""
    all_files = set(root.rglob('*'))
    logger.debug(all_files)

    truth_files = (
        list(root.rglob('*.py'))
        + list(root.rglob('sample*'))
        + list(root.rglob('python-zipfile*'))
        + list(root.rglob('.git*'))
    )
    logging.debug('truth_files=%s', truth_files)

    wanted_files = all_files.difference(truth_files)
    logger.debug('wanted_files=%s', wanted_files)
    [file.unlink(missing_ok=True) for file in wanted_files if file.is_file()]
    [shutil.rmtree(file) for file in wanted_files if file.is_dir()]
