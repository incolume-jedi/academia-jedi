import typing
import logging
import xmltodict
from pathlib import Path
from collections import OrderedDict
from dataclasses import dataclass


FILES_XML: typing.Final = list(Path(__file__).parent.joinpath('NFs_Finais').rglob("*.xml"))
logging.debug(FILES_XML)


def open_files(file: Path|str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict."""
    file = Path(file)
    with file.open(mode) as f:
        documento = xmltodict.parse(f)
    return documento


@dataclass
class NFe:
    """"""


def tratativa0():
    """Carregar conteúdo do arquivo XML em dict."""
    logging.debug(FILES_XML)
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brota'))
    logging.debug(xml_file)
    return open_files(xml_file)


def tratativa1():
    """Capturar campo de NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brota'))
    logging.debug(xml_file)
    documento = open_files(xml_file)
    return documento['nfeProc']['NFe']['infNFe']['ide']['cUF']


def tratativa2():
    """Capturar campo de Nome."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brota'))
    logging.debug(xml_file)
    documento = open_files(xml_file)
    return documento['nfeProc']['NFe']['infNFe']['dest']['xNome']


def tratativa3():
    """Retorna Informações da NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brota'))
    logging.debug(xml_file)
    documento = open_files(xml_file)
    return documento['nfeProc']['NFe']['infNFe']


def tratativa4():
    """Retorna o Valor total da NFe."""
    return tratativa3()['total']['ICMSTot']['vNF']


def tratativa5():
    """Retorna o Nome e CNPF do Emissor."""
    return tratativa3()['emit']['xNome'], tratativa3()['emit']['CNPJ']


def tratativa6():
    """Resposta do problema proposto."""
    resposta = {
        'valor_total': tratativa3()['total']['ICMSTot']['vNF'],
        'cnpj_vendeu': tratativa3()['emit']['CNPJ'],
        'nome_vendeu': tratativa3()['emit']['xNome'],
        'cpf_comprou': tratativa3()['dest']['CPF'],
        'nome_comprou': tratativa3()['dest']['xNome'],
        'lista_produtos': [(prod['prod']['qCom'], prod['prod']['xProd'], prod['prod']['vUnCom'], prod['prod']['vProd']) for prod in tratativa3()['det']],
    }
    return resposta


def tratativa7():
    """"""


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
