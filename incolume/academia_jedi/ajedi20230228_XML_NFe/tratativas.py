import typing
import logging
import xmltodict
from pathlib import Path
from collections import OrderedDict
from dataclasses import dataclass, field, asdict, astuple

FILES_XML: typing.Final = list(
    Path(__file__).parent.joinpath('NFs_Finais').rglob("*.xml"))
logging.debug(FILES_XML)


def open_files(file: Path | str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict."""
    file = Path(file)
    with file.open(mode) as f:
        documento = xmltodict.parse(f)
    return documento


def get_info_nfe(file: Path| str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict retornando as informações da NFe."""
    return open_files(file, mode)['nfeProc']['NFe']['infNFe']


def get_content_nfe(xml_file: Path|str, tp: str = '') -> OrderedDict:
    """Resposta do problema para outra NFe."""
    logging.debug(xml_file)
    documento = get_info_nfe(xml_file)
    resposta = NFe(**{
        'valor_total': documento['total']['ICMSTot']['vNF'],
        'cnpj_vend': documento['emit']['CNPJ'],
        'nome_vend': documento['emit']['xNome'],
        'cpf_comp': documento['dest']['CPF'],
        'nome_comp': documento['dest']['xNome'],
        'itens_nf': [
            ItensNFe(*(
                prod['prod']['xProd'],
                float(prod['prod']['qCom']),
                float(prod['prod']['vUnCom']),
                float(prod['prod']['vProd'])
            ))
            for prod in documento['det']],
    })
    match tp:
        case 'dict':
            return asdict(resposta)
        case 'tuple':
            return astuple(resposta)
        case _:
            return resposta

@dataclass
class ItensNFe:
    """Produtos."""
    nome: str
    quantia: int = field(default=0)
    valor_unitario: float = field(default=0)
    valor_total: float = field(default=0)


@dataclass
class NFe:
    """Nota Fistal Eletrônica."""
    valor_total: float
    cnpj_vend: str
    nome_vend: str
    cpf_comp: str
    nome_comp: str
    nome_fantasia: str = field(default='')
    itens_nf: typing.List[ItensNFe] = field(default_factory=list)


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
        'lista_produtos': [(float(prod['prod']['qCom']), prod['prod']['xProd'],
                            prod['prod']['vUnCom'], prod['prod']['vProd']) for
                           prod in tratativa3()['det']],
    }
    return resposta


def tratativa7():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = open_files(xml_file)['nfeProc']['NFe']['infNFe']
    resposta = {
        'valor_total': documento['total']['ICMSTot']['vNF'],
        'cnpj_vendeu': documento['emit']['CNPJ'],
        'nome_vendeu': documento['emit']['xNome'],
        'cpf_comprou': documento['dest']['CPF'],
        'nome_comprou': documento['dest']['xNome'],
        'lista_produtos': [(float(prod['prod']['qCom']), prod['prod']['xProd'],
                            prod['prod']['vUnCom'], prod['prod']['vProd']) for
                           prod in documento['det']],
    }
    return resposta


def tratativa8():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = open_files(xml_file)['nfeProc']['NFe']['infNFe']
    resposta = NFe(**{
        'valor_total': documento['total']['ICMSTot']['vNF'],
        'cnpj_vend': documento['emit']['CNPJ'],
        'nome_vend': documento['emit']['xNome'],
        'cpf_comp': documento['dest']['CPF'],
        'nome_comp': documento['dest']['xNome'],
        'itens_nf': [
            ItensNFe(*(
                prod['prod']['xProd'],
                float(prod['prod']['qCom']),
                float(prod['prod']['vUnCom']),
                float(prod['prod']['vProd'])
            ))
            for prod in documento['det']],
    })
    return resposta


def tratativa9():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = get_info_nfe(xml_file)
    resposta = NFe(**{
        'valor_total': documento['total']['ICMSTot']['vNF'],
        'cnpj_vend': documento['emit']['CNPJ'],
        'nome_vend': documento['emit']['xNome'],
        'cpf_comp': documento['dest']['CPF'],
        'nome_comp': documento['dest']['xNome'],
        'itens_nf': [
            ItensNFe(*(
                prod['prod']['xProd'],
                float(prod['prod']['qCom']),
                float(prod['prod']['vUnCom']),
                float(prod['prod']['vProd'])
            ))
            for prod in documento['det']],
    })
    return asdict(resposta)


def tratativa10():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_nfe(xml_file)


def tratativa11():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_nfe(xml_file, 'dict')


def tratativa12():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_nfe(xml_file, 'tuple')


def tratativa13():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_nfe(xml_file)


def tratativa14():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_nfe(xml_file, 'dict')


def tratativa15():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_nfe(xml_file, 'tuple')


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
