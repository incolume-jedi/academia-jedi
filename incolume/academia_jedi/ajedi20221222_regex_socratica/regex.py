import re
from functools import wraps
from collections.abc import Callable

names = (
    'Francois',
    'Rupert Cambrige',
    'Mike Whitney',
    'Sagun Khatri',
    'Nick Francesco',
    'Pickles',
    'K5ANR',
    'Bryan Ander Berge',
    'Bob   Finger',
    'Carlos Alterto',
    'SussexCambrige',
    'Jedi Incolume',
    'João das Colves',
    'm!sha',
    'http://brito.blog.incolume.com.br',
    'https://brito.blog.incolume.com.br',
    'ftp://ftp.incolume.com.br',
    'https://snu.socratica.com/python',
)


def show_examples(func: Callable):
    @wraps(func)
    def inner(*args, **kwargs):
        print('===')
        print(func.__name__)
        print(f'{args=} {kwargs=}')
        print(f'   >>> {func.__doc__}')
        print('---')
        func(*args, **kwargs)
        print('---\n')

    return inner


@show_examples
def ex01():
    """Find people with first and last name only."""
    regex = r'^\w+ \w+$'
    for name in names:
        result = re.search(regex, name)
        if result:
            print(name)


@show_examples
def ex02():
    """Find people with first and last name only."""
    regex = r'^\w+\s+\w+$'
    for name in names:
        result = re.search(regex, name)
        if result:
            print(name)


@show_examples
def ex03():
    """Search for word char sequence starting with C."""
    regex = r'C\w*'
    for name in names:
        match = re.match(regex, name)
        if match:
            print(name)
            print(match.start())
            print(match.end())


@show_examples
def ex04():
    """Search for word char sequence starting with C."""
    regex = r'C\w*'
    for name in names:
        match = re.match(regex, name)
        if match:
            print(name)
            print(match.span())


@show_examples
def ex05():
    """Test for first name and last name by groups."""
    regex = r'^(\w+)\s+(\w+)$'
    for name in names:
        match = re.search(regex, name)
        if match:
            print(name)
            print(match.group(1))
            print(match.group(2))


@show_examples
def ex06():
    """Test for first name, midle name and last name by named groups."""
    regex = r'^(?P<fn>\w+)\s+(?P<mn>\w+)\s+(?P<ln>\w+)$'
    for name in names:
        match = re.search(regex, name)
        if match:
            print(name)
            print(
                match.group('fn'),
                match.group('mn'),
                match.group('ln'),
                sep='\n',
                end='\n\n',
            )


@show_examples
def ex07():
    """Detect unique name."""
    regex = '^[a-zA-Z!]+$'
    for name in names:
        if re.search(regex, name):
            print(name)


@show_examples
def ex08():
    """Scan for blocks of lower case letters."""
    regex = r'[a-z]+'
    for name in names:
        matches = re.findall(regex, name)
        if matches:
            print(matches)


@show_examples
def ex09():
    """Scan for blocks of lower case letters."""
    regex = r'[a-z]+'
    for name in names:
        matches = re.findall(regex, name)
        for match in matches:
            print(match)


@show_examples
def ex10():
    """Test if string starts with http or https."""
    regex = r'https?'
    for value in names:
        if re.match(regex, value):
            print(value)


@show_examples
def ex11():
    """Test if string starts with http, https or ftp."""
    regex = r'(ht|f)tps?'
    for value in names:
        if re.match(regex, value):
            print(value)


@show_examples
def ex12():
    """Test if URL valid."""
    regex = r'(ht|f)tps?://snu.\w+.(org|com)'
    for value in names:
        if re.match(regex, value):
            print(value)


def run():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()
    ex07()
    ex08()
    ex09()
    ex10()
    ex11()
    ex12()


if __name__ == '__main__':  # pragma: no cover
    run()
