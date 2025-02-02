"""XML handler."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import os
from pathlib import Path

import xmltodict

# abrir e ler o arquivo


def ler_xml_danfe(nota: Path | str) -> dict[str, list[str]]:
    """XML read."""
    nota = Path(nota)
    with nota.open('rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']
    produtos = dic_notafiscal['det']
    lista_produtos = []
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))
    return {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [lista_produtos],
    }


def ler_xml_servico(nota: Path | str) -> dict[str, list[str]]:
    """XML service."""
    nota = Path(nota)
    with nota.open('rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse'][
        'CompNfse'
    ]['Nfse']['InfNfse']

    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador'][
        'Cnpj'
    ]
    nome_vendeu = dic_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafiscal['TomadorServico']['IdentificacaoTomador'][
        'CpfCnpj'
    ]['Cnpj']
    nome_comprou = dic_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dic_notafiscal['Servico']['Discriminacao']
    return {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [produtos],
    }


lista_arquivos = os.listdir(
    'NFs Finais',
)  # lista os nomes dos arquivos de uma pasta

for arquivo in lista_arquivos:  # para cada arquivo
    if 'xml' in arquivo:  # se tem xml no nome do arquivo
        if 'DANFE' in arquivo:  # se tem DANFE no nome do arquivo
            print(
                ler_xml_danfe(f'NFs Finais/{arquivo}'),
            )  # rodar o leitor de XML de DANFE para esse arquivo
        else:
            print(ler_xml_servico(f'NFs Finais/{arquivo}'))

#


# caso queria adicionar todas as NFs em um mesmo arquivo Excel:
#
# for arquivo in arquivos:
#     if 'xml' in arquivo:
#         if 'DANFE' in arquivo:
