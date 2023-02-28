import typing
import logging
import xmltodict
from pathlib import Path
from collections import OrderedDict


FILES_XML: typing.Final = list(Path(__file__).parent.joinpath('NFs_Finais').rglob("*.xml"))
logging.debug(FILES_XML)


def open_files(file: Path|str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict."""
    file = Path(file)
    with file.open(mode) as f:
        documento = xmltodict.parse(f)
    return documento


def tratativa0():
    """Carregar conteúdo do arquivo XML em dict."""
    logging.debug(FILES_XML)
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brota'))
    logging.debug(xml_file)
    print(open_files(xml_file))


def tratativa1():
    """Nop."""


def run():
    """Running it."""
    functions: typing.List[typing.Callable] = [
        value for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print('    >>> {}'.format(func.__doc__))
        try:
            if result := func():
                print(result)
        except ValueError as e:
            logging.error(f'{e.__class__.__name__}: {e}')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
