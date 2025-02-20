"""Manipulação de NFe."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import logging
import re
import typing
from collections import OrderedDict
from dataclasses import asdict, astuple, dataclass, field
from pathlib import Path

import pandas as pd
import xmltodict

FILES_XML: typing.Final = list(
    Path(__file__).parent.joinpath('NFs_Finais').rglob('*.xml'),
)
logging.debug(FILES_XML)


@dataclass
class ItensNFe:
    """Produtos."""

    nome: str
    quantia: int = field(default=0)
    valor_unitario: float = field(default=0)
    valor_total: float = field(default=0)


@dataclass
class ServicoNFe:
    """Serviços."""

    description: str
    quantia: int = field(default=1)


@dataclass
class NFe:
    """Nota Fistal Eletrônica."""

    valor_total: float
    cnpj_vend: str
    nome_vend: str
    cpf_comp: str
    nome_comp: str
    nome_fantasia: str = field(default='')
    itens_nf: list[ItensNFe | ServicoNFe] = field(default_factory=list)


def open_files(file: Path | str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict."""
    file = Path(file)
    with file.open(mode) as f:
        return xmltodict.parse(f)


def get_info_nfe(file: Path | str, mode: str = 'rb') -> OrderedDict:
    """Abre arquivos XML e converte para dict.

    :file: Arquivo de NFe
    :mode: Mode de leitura para Arquivo NFe
    :return: retorna as informações da NFe.
    """
    return open_files(file, mode)['nfeProc']['NFe']['infNFe']


def get_content_service_nfe(
    xml_file: Path | str,
    tp: str = '',
) -> NFe | typing.Container:
    """Retorna elementos da NFe de serviços."""
    logging.debug(xml_file)
    documento = open_files(xml_file)['ConsultarNfseResposta']['ListaNfse'][
        'CompNfse'
    ]['Nfse']['InfNfse']
    resposta = NFe(
        valor_total=documento['Servico']['Valores']['ValorServicos'],
        cnpj_vend=documento['PrestadorServico']['IdentificacaoPrestador'][
            'Cnpj'
        ],
        nome_vend=documento['PrestadorServico']['RazaoSocial'],
        cpf_comp=documento['TomadorServico']['IdentificacaoTomador'][
            'CpfCnpj'
        ]['Cnpj'],
        nome_comp=documento['TomadorServico']['RazaoSocial'],
        itens_nf=ServicoNFe(documento['Servico']['Discriminacao']),
    )
    match tp:
        case 'dict':
            return asdict(resposta)
        case 'tuple':
            return astuple(resposta)
        case _:
            return resposta


@dataclass(slots=True)
class MatchRegex(str):
    """MatchRegex class."""

    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        """Equal class."""
        self.match = re.search(pattern, self.string)
        return self.match is not None

    def __getitem__(self, group):
        """Gettem class."""
        return self.match[group]


def get_content_danfe_nfe(
    xml_file: Path | str,
    tp: str = '',
) -> NFe | typing.Container:
    """Retorna elemento da NFe Danfe."""
    logging.debug(xml_file)
    documento = get_info_nfe(xml_file)
    resposta = NFe(
        valor_total=documento['total']['ICMSTot']['vNF'],
        cnpj_vend=documento['emit']['CNPJ'],
        nome_vend=documento['emit']['xNome'],
        cpf_comp=documento['dest']['CPF'],
        nome_comp=documento['dest']['xNome'],
        itens_nf=[
            ItensNFe(
                *(
                    prod['prod']['xProd'],
                    float(prod['prod']['qCom']),
                    float(prod['prod']['vUnCom']),
                    float(prod['prod']['vProd']),
                ),
            )
            for prod in documento['det']
        ],
    )
    match tp:
        case 'dict':
            return asdict(resposta)
        case 'tuple':
            return astuple(resposta)
        case _:
            return resposta


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
    return {
        'valor_total': tratativa3()['total']['ICMSTot']['vNF'],
        'cnpj_vendeu': tratativa3()['emit']['CNPJ'],
        'nome_vendeu': tratativa3()['emit']['xNome'],
        'cpf_comprou': tratativa3()['dest']['CPF'],
        'nome_comprou': tratativa3()['dest']['xNome'],
        'lista_produtos': [
            (
                float(prod['prod']['qCom']),
                prod['prod']['xProd'],
                prod['prod']['vUnCom'],
                prod['prod']['vProd'],
            )
            for prod in tratativa3()['det']
        ],
    }


def tratativa7():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = open_files(xml_file)['nfeProc']['NFe']['infNFe']
    return {
        'valor_total': documento['total']['ICMSTot']['vNF'],
        'cnpj_vendeu': documento['emit']['CNPJ'],
        'nome_vendeu': documento['emit']['xNome'],
        'cpf_comprou': documento['dest']['CPF'],
        'nome_comprou': documento['dest']['xNome'],
        'lista_produtos': [
            (
                float(prod['prod']['qCom']),
                prod['prod']['xProd'],
                prod['prod']['vUnCom'],
                prod['prod']['vProd'],
            )
            for prod in documento['det']
        ],
    }


def tratativa8():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = open_files(xml_file)['nfeProc']['NFe']['infNFe']
    return NFe(
        valor_total=documento['total']['ICMSTot']['vNF'],
        cnpj_vend=documento['emit']['CNPJ'],
        nome_vend=documento['emit']['xNome'],
        cpf_comp=documento['dest']['CPF'],
        nome_comp=documento['dest']['xNome'],
        itens_nf=[
            ItensNFe(
                *(
                    prod['prod']['xProd'],
                    float(prod['prod']['qCom']),
                    float(prod['prod']['vUnCom']),
                    float(prod['prod']['vProd']),
                ),
            )
            for prod in documento['det']
        ],
    )


def tratativa9():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    logging.debug(xml_file)
    documento = get_info_nfe(xml_file)
    resposta = NFe(
        valor_total=documento['total']['ICMSTot']['vNF'],
        cnpj_vend=documento['emit']['CNPJ'],
        nome_vend=documento['emit']['xNome'],
        cpf_comp=documento['dest']['CPF'],
        nome_comp=documento['dest']['xNome'],
        itens_nf=[
            ItensNFe(
                *(
                    prod['prod']['xProd'],
                    float(prod['prod']['qCom']),
                    float(prod['prod']['vUnCom']),
                    float(prod['prod']['vProd']),
                ),
            )
            for prod in documento['det']
        ],
    )
    return asdict(resposta)


def tratativa10():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_danfe_nfe(xml_file)


def tratativa11():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_danfe_nfe(xml_file, 'dict')


def tratativa12():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    return get_content_danfe_nfe(xml_file, 'tuple')


def tratativa13():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_danfe_nfe(xml_file)


def tratativa14():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_danfe_nfe(xml_file, 'dict')


def tratativa15():
    """Resposta do problema para outra NFe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Nespresso'))
    return get_content_danfe_nfe(xml_file, 'tuple')


def tratativa16():
    """Converte para Dataframe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    dados = get_content_danfe_nfe(xml_file, 'dict')
    nota_df = pd.DataFrame.from_dict(dados)
    print(nota_df)


def tratativa17():
    """Converte para Dataframe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    dados = get_content_danfe_nfe(xml_file, 'tuple')
    nota_df = pd.DataFrame(dados).T
    columns = [
        'valor_total',
        'cnpj_vend',
        'nome_vend',
        'cpf_comp',
        'nome_comp',
        'nome_fantasia',
        'itens_nf',
    ]
    nota_df.columns = columns
    print(nota_df)


def tratativa18():
    """Converte para Dataframe."""
    xml_file = next(x for x in FILES_XML if x.name.__contains__('Brot'))
    dados = get_content_danfe_nfe(xml_file, 'tuple')
    columns = [
        'valor_total',
        'cnpj_vend',
        'nome_vend',
        'cpf_comp',
        'nome_comp',
        'nome_fantasia',
        'itens_nf',
    ]
    nota_df = pd.DataFrame(dados, index=columns).T
    print(nota_df)


def tratativa19():
    """Multiplas excuções danfe."""
    for xml_file in (x for x in FILES_XML if x.name.__contains__('DANFE')):
        print(get_content_danfe_nfe(xml_file, 'dict'))


def tratativa20():
    """Nota de Serviço carioca."""
    logging.debug(
        xml_file := next(
            x for x in FILES_XML if x.name.__contains__('Carioca')
        ),
    )
    return get_content_service_nfe(xml_file)


def tratativa21():
    """Multiplas execuções NFe danfe + carioca."""
    for xml_file in FILES_XML:
        print(xml_file)
        if xml_file.as_posix().__contains__('Carioca'):
            print(get_content_service_nfe(xml_file, 'dict'))
        else:
            print(get_content_danfe_nfe(xml_file, 'dict'))


def tratativa22():
    """Multiplas execuções NFe com match/case."""
    for xml_file in FILES_XML:
        print(xml_file)
        match xml_file.as_posix().__contains__('Carioca'):
            case True:
                print(get_content_service_nfe(xml_file, 'dict'))
            case _:
                print(get_content_danfe_nfe(xml_file, 'dict'))


def tratativa23():
    """Multiplas execuções NFe com regex match/case."""
    for xml_file in FILES_XML:
        logging.debug(xml_file)

        match MatchRegex(xml_file.as_posix()):
            case 'Carioca':
                print(1, xml_file)
                print(get_content_service_nfe(xml_file))
            case 'DANFE':
                print(2, xml_file)
                print(get_content_danfe_nfe(xml_file))
            case _:
                msg = f'NFe {xml_file} do not match any case configured.'
                raise AssertionError(
                    msg,
                )


def run():
    """Running it."""
    functions: list[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug('%s %s', type(func), func.__name__)
        print(f'--- {func.__name__} ---')
        print(f'    >>> {func.__doc__}')
        try:
            if result := func():
                print(result)
        except (TypeError, ValueError) as e:
            logging.exception('%s', e.__class__.__name__)
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
