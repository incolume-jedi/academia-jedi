"""Module."""

from __future__ import annotations

import shutil
from pathlib import Path

from config import settings
from icecream import ic

ic.disable()
if settings.debug_mode:
    ic.enable()

path_files: Path = Path(__file__).parent.joinpath('files/arquivos_desafio')


def organizer_dir(
    path_files_in: Path | None = None,
    path_files_out: Path | None = None,
    output_base: Path | None = None,
) -> Path:
    """Organizar pasta de arquivos."""
    path_files_in = path_files_in or Path()
    output_base = output_base or path_files_in
    path_files_out = path_files_out or output_base / 'backup'

    result = {}
    ic(result)
    for file in (f for f in path_files_in.iterdir() if f.is_file()):
        ic(file)
        result.setdefault(file.suffix.casefold().strip('.'), []).append(file)
        dir_out = path_files_out / file.suffix.casefold().strip('.')
        dir_out.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, dir_out / file.name)
    ic(result)
    return path_files_out


def gen_bkp(
    path_files: Path | None = None,
    file_output: Path | None = None,
    type_format: str = 'zip',
) -> Path:
    """Generate a backup."""
    file_output = file_output or path_files / 'backup'
    return Path(
        shutil.make_archive(
            base_name=file_output,
            format=type_format,
            root_dir=path_files,
        ),
    )


if __name__ == '__main__':
    path = Path(
        r'C:\Users\ricardobn\AppData\Local\Temp\TestOrganizer\test_gen',
    )
    type_format = 'tar'
    ic(bkp := organizer_dir(path_files, output_base=path))
    ic(
        filecompress := gen_bkp(
            path_files=bkp,
            file_output=path,
            type_format=type_format,
        ),
    )
    shutil.unpack_archive(
        filecompress,
        extract_dir=path / 'restore',
        format=type_format,
    )
