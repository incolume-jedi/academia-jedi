"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample, logger


def run():
    """Run it."""
    archive = zipfile.ZipFile(filezip_sample, mode='r')

    # Use archive in different parts of your code
    print(archive.printdir())

    # Close the archive when you're done
    archive.close()
    logger.info(archive)
    print(archive)


if __name__ == '__main__':
    run()
