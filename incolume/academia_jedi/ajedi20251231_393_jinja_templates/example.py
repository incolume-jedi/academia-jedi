"""Example."""

import inspect
import tempfile
from collections.abc import Container
from pathlib import Path
from typing import Final

import jinja2
from icecream import ic

students_db: Container[dict] = [
    {'name': 'Brito', 'score': 100},
    {'name': 'Ana Brito', 'score': 95},
    {'name': 'Ada Brito', 'score': 85},
    {'name': 'Eliana Brito', 'score': 70},
    {'name': 'Naome Brito', 'score': 60},
]


def example1():
    """Docstring para example1."""
    env = jinja2.Environment(autoescape=True)
    template = env.from_string('Hello {{name}}!')
    ic(template.render(name='World'))


def example_good_msg(students: Container[dict] | None = None):
    """Docstring para example_good_msg."""
    MAX_SCORE: Final[int] = 100
    TEST_NAME: Final[str] = 'Python Challenge'
    tmpl_dir = Path(__file__).parent.joinpath('templates')
    ic(tmpl_dir.exists())

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(tmpl_dir),
        autoescape=True,
    )
    template = env.get_template('good_msg.tmpl')
    students = students or students_db

    for student in students:
        name: str = student.get('name')
        fout: Path = Path(
            tempfile.gettempdir(),
        ).joinpath(
            inspect.stack()[0][3],
            f'{template.name.split(".")[0]}-{name.casefold().replace(" ", "-")}.txt',
        )
        fout.parent.mkdir(parents=True, exist_ok=True)
        content = template.render(
            student,
            max_score=MAX_SCORE,
            test_name=TEST_NAME,
        )

        fout.write_text(content)
        ic(f'{fout} is {fout.is_file()}')


def example_msg_for_all(students: Container[dict] | None = None):
    """Docstring para example_msg_for_all."""
    MAX_SCORE: Final[int] = 100
    TEST_NAME: Final[str] = 'Python Challenge'

    tmpl_dir = Path(__file__).parent.joinpath('templates')
    ic(tmpl_dir.exists())

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(tmpl_dir),
        autoescape=True,
    )
    template = env.get_template('msg4all.tmpl')
    students = students or students_db

    for student in students:
        name: str = student.get('name')
        fout: Path = Path(
            tempfile.gettempdir(),
        ).joinpath(
            inspect.stack()[0][3],
            f'{template.name.split(".")[0]}-{name.casefold().replace(" ", "-")}.txt',
        )
        fout.parent.mkdir(parents=True, exist_ok=True)
        content = template.render(
            student,
            max_score=MAX_SCORE,
            test_name=TEST_NAME,
        )

        fout.write_text(content)
        ic(f'{fout} is {fout.is_file()}')


def run():
    """Run it."""
    example1()
    example_good_msg()
    example_msg_for_all()


if __name__ == '__main__':
    run()
