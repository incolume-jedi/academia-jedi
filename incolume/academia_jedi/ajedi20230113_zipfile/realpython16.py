"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample, logger


def run():
    """Run it."""
    logger.debug(filezip_sample.parts)

    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        logger.debug(archive.filename)
        text = archive.read('hello.txt').decode(encoding='utf-8')

    print(text)


if __name__ == '__main__':
    run()
