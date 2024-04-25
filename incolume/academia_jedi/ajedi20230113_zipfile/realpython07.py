import zipfile
from pathlib import Path

directory = Path(__file__).parent

hello = directory.joinpath('hello.txt')
hello.write_text('hello')
hello.with_stem('new_hello').write_text('hello again.')


def run():
    with zipfile.ZipFile(directory / 'hello.zip', mode='r') as archive:
        print(archive.infolist())
        print(archive.namelist())
        print(directory)

        info = archive.getinfo(Path(*hello.parts[1:]).as_posix())
    print(
        f'{info.file_size=}\n{info.compress_size=}\n{info.filename=}\n{info.date_time=}\n',
    )


if __name__ == '__main__':
    run()
