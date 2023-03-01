import xmltodict

# abrir e ler o arquivo

def ler_xml_danfe(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    # print(documento)
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
    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [lista_produtos],
    }
    return resposta


def ler_xml_servico(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    # print(documento)
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dic_notafiscal['Servico']['Discriminacao']
    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [produtos],
    }
    return resposta

import os

lista_arquivos = os.listdir("NFs Finais") # lista os nomes dos arquivos de uma pasta

for arquivo in lista_arquivos: # para cada arquivo
    if 'xml' in arquivo: # se tem xml no nome do arquivo
        if 'DANFE' in arquivo: # se tem DANFE no nome do arquivo
            print(ler_xml_danfe(f'NFs Finais/{arquivo}')) # rodar o leitor de XML de DANFE para esse arquivo
        else:
            print(ler_xml_servico(f'NFs Finais/{arquivo}'))


# valor_total, produtos/servicos (valores), cnpj_vendeu, nome_vendeu, cpf/cnpj_comprou, nome_comprou
# import pandas as pd
#
# tabela = pd.DataFrame.from_dict(resposta)
# tabela.to_excel("NFs.xlsx")


# caso queria adicionar todas as NFs em um mesmo arquivo Excel:
# import pandas as pd
# arquivos = os.listdir("NFs Finais")
#
# df_final = pd.DataFrame()
# for arquivo in arquivos:
#     if 'xml' in arquivo:
#         if 'DANFE' in arquivo:
#             df = pd.DataFrame.from_dict(ler_xml_danfe(f"NFs Finais/{arquivo}"))
#         else:
#             df = pd.DataFrame.from_dict(ler_xml_servico(f'NFs Finais/{arquivo}'))
#         df_final = df_final.append(df)
# print(df_final)
# df_final.to_excel('NFs.xlsx', index=False)