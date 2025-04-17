"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir


def run():
    """Run it."""
    filenames = base_dir.rglob('*.txt')

    with zipfile.ZipFile(
        base_dir.joinpath('output_dir', 'multiple_files.zip'),
        mode='w',
    ) as archive:
        for filename in filenames:
            archive.write(filename)


if __name__ == '__main__':
    run()
