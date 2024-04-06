"""Solução dos exercícios estrutura de decisão."""
import datetime
import operator
from collections import namedtuple

from unidecode import unidecode


def exercicio01(num1: float, num2: float) -> float:
    """Faça um Programa que peça dois números e imprima o maior deles."""
    return max(num1, num2)


def exercicio02(num: float) -> str:
    """Positivo ou Negativo.
    Faça um Programa que peça um valor e mostre
    na tela se o valor é positivo ou negativo.
    """
    if num == 0:
        return 'neutro'
    return 'negativo' if num < 0 else 'positivo'


def exercicio03(sexo: str) -> str:
    """Faça um Programa que verifique se uma letra digitada é "F" ou "M".

    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    """
    valores = {
        'F': 'F - Feminino',
        'M': 'M - Masculino',
    }

    return valores.get(str(sexo).upper(), 'Sexo Inválido')


def exercicio04(letra: str) -> str:
    """Vogal ou consoante.
    Faça um Programa que verifique se uma letra digitada
    é vogal ou consoante.
    """
    vogais = 'AEIOU'

    def isVogal(letra: str) -> bool:
        return letra.upper() in vogais

    return 'Vogal' if isVogal(letra) else 'Consoante'


def exercicio05(nota1: float, nota2: float) -> str:
    """Faça um programa para a leitura de duas notas parciais de um aluno.

    O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
    """
    mensao = ['Reprovado', 'Aprovado', 'Aprovado com Distinção']
    media = (nota1 + nota2) / 2
    return mensao[int(media >= 7.0) + int(media == 10.0)]


def exercicio06(*args) -> float:
    """Faça um Programa que leia três números e mostre o maior deles."""
    return max(args)


def exercicio07(*args) -> tuple:
    """Maior e menor.
    Faça um Programa que leia três números e mostre
    o maior e o menor deles.
    """
    maior = -999999999999999999
    menor = 9999999999999999999

    for n in args:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    return maior, menor


def exercicio08(*args) -> float:
    """Faça um programa que pergunte o preço de três produtos
    e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
    """
    return exercicio07(*args)[-1]


def exercicio09(*args):
    """Faça um Programa que leia três números
    e mostre-os em ordem decrescente.
    """
    return sorted(args, reverse=True)


def exercicio10(turno: str):
    """Checar turno.

    Faça um Programa que pergunte em que turno você estuda.

        Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
        Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
        ou "Valor Inválido!", conforme o caso.
    """
    turnos = {
        'm': 'Bom Dia!',
        'v': 'Boa Tarde!',
        'n': 'Boa Noite!',
        'matutino': 'Bom Dia!',
        'vespertino': 'Boa Tarde!',
        'noturno': 'Boa Noite!',
    }
    try:
        return turnos[turno.casefold()]
    except KeyError:
        raise ValueError('Turno inválido: "%s".' % turno)


def exercicio11(salario: float) -> str:
    """Reajustar salário.

    As Organizações Tabajara resolveram dar um aumento de salário aos seus
    colaboradores e lhe contrataram para desenvolver o programa que
    calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste
    segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento
    ser realizado, informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.
    """
    # salarios = [280, 700, 1500, 1500.01]
    # ajustes = [.2, .15, .1, .05]

    def reajuste(salario: float) -> tuple:
        """Calcular reajuste."""
        taxa = 0.2
        if salario > 1500:
            taxa = 0.05
        if 700 < salario <= 1500:
            taxa = 0.1
        if 280 < salario <= 700:
            taxa = 0.15
        return taxa, salario * taxa

    def saida(salario: float) -> str:
        """Resultado do problema."""
        tax, aumento = reajuste(salario)
        return (
            f'Salário atual: R$ {salario: .2f}\n '
            f'aumento: {tax * 100} %\n aumento: R$ {aumento: .2f}\n '
            f'Salário novo: R$ {salario + aumento:.2f}'
        )

    return saida(salario)


def exercicio12(valor_hora: float, quantia_hora: float) -> str:
    """Faça um programa para o cálculo de uma folha de pagamento.

    Sabendo que os descontos são do Imposto de Renda, que depende do
    salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
     corresponde a 11% do Salário Bruto, mas não é descontado
     (é a empresa que deposita). O Salário Líquido corresponde ao
     Salário Bruto menos os descontos. O programa deverá pedir ao usuário
      o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
    informações, dispostas conforme o exemplo abaixo. No exemplo o
    valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
    """
    taxa_ir = {900: 0, 1500: 5, 2500: 10, 2500.01: 20}
    taxa_inss = 0.1
    taxa_fgts = 0.11
    sal_bruto = valor_hora * quantia_hora
    inss = sal_bruto * taxa_inss
    fgts = sal_bruto * taxa_fgts
    ir = 0
    descontos = ir + fgts

    print(
        f"""
            Salário Bruto: ({valor_hora} * {quantia_hora}): R$ {sal_bruto}
            (-) IR (5%)                     : R$   {ir}
            (-) INSS ( 10%)                 : R$  {inss}
            FGTS (11%)                      : R$  {fgts}
            Total de descontos              : R$  {descontos}
            Salário Liquido                 : R$  {sal_bruto - descontos}""",
    )


def exercicio13(dia: int) -> str:
    """Faça um Programa que leia um número e exiba
    o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido.
    """
    dow = {
        1: '1-Domingo',
        2: '2-Segunda',
        3: '3-Terça',
        4: '4-Quarta',
        5: '5-Quinta',
        6: '6-Sexta',
        7: '7-Sabado',
    }
    return dow.get(dia, 'valor inválido')


def exercicio14(*args) -> str:
    """Faça um programa que lê as duas notas parciais obtidas por um aluno
    numa disciplina ao longo de um semestre, e calcule a sua média.

    A atribuição de conceitos obedece à tabela abaixo:
     Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
    O algoritmo deve mostrar na tela as notas, a média, o conceito
    correspondente e a mensagem “APROVADO” se o conceito for A, B, C
    ou “REPROVADO” se o conceito for D ou E.
    """
    mensagens = {
        'A': 'APROVADO',
        'B': 'APROVADO',
        'C': 'APROVADO',
        'D': 'REPROVADO',
        'E': 'REPROVADO',
    }
    try:
        args = tuple(float(x) for x in args)
    except ValueError:
        raise ValueError('Somente valores numéricos.')
    media = sum(args) / len(args)

    def calc_conceito(media: float) -> str:
        """Calcular conceito."""
        if 9 <= media <= 10:
            return 'A'
        if 7.5 <= media <= 9:
            return 'B'
        if 6 <= media <= 7.5:
            return 'C'
        if 4 <= media <= 6:
            return 'D'
        return 'E'

    def mostrar_resultado(media: float) -> str:
        """Apresentação do resultado."""
        conceito = calc_conceito(media)
        return (f'Notas: {args}, Média: {media}, '
                f'Conceito: {conceito} "{mensagens[conceito]}"')

    return mostrar_resultado(media)


def exercicio15(a: int, b: int, c: int) -> str:
    """Faça um Programa que peça os 3 lados de um triângulo.
    O programa deverá informar se os valores podem ser um triângulo.
    Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de
    quaisquer dois lados for maior que o terceiro;

    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
    """
    result: str = ''
    if (a + b) < c:
        result = 'Não forma triângulo.'
    elif a == b == c:
        result = 'Triângulo equilátero'
    elif (a == b) or (b == c) or (a == c):
        result = 'Triângulo isósceles'
    elif not (a == b == c):
        result = 'Triângulo escaleno'
    return result


def exercicio16():
    """Faça um programa que calcule as raízes de uma equação do segundo grau,
    na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
    e fazer as consistências, informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero, a equação não é
    do segundo grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real; informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raiz reais;
    informe-as ao usuário;
    """
    values = []

    temp = int(input('digite o valor para "a": '))
    if temp == 0:
        return f'a={temp}. Não é uma equação de segundo grau.'
    values.append(temp)
    values.append(int(input('digite o valor para "b": ')))
    values.append(int(input('digite o valor para "c": ')))
    a, b, c = values

    def delta(*values):
        a, b, c = values
        return b ** 2 - 4 * a * c

    def x(*values):
        a, b, c = values
        d = delta(a, b, c)
        if d < 0:
            return f'delta={d}. Não possui raízes reais.'
        if d == 0:
            return (
                f'delta={d}. Possui apenas uma raiz real: '
                f'{(-b + d ** (1 / 2)) / (2 * a)}'
            )
        if d > 0:
            return (
                f'x = {(-b + d ** (1 / 2)) / (2 * a)} '
                f'ou {(-b - d ** (1 / 2)) / (2 * a)}'
            )

    return x(*values)


def exercicio17(ano: int) -> bool:
    """Faça um Programa que peça um número correspondente a
    um determinado ano e em seguida informe se este ano é ou não bissexto.

    Obs:
         Bissexto - Um ano é bissexto se ele for divisível por 400 ou se ele
       for divisível por 4 e não por 100.
    """
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        return True
    return False


def exercicio18(data: str):
    """Faça um Programa que peça uma data no formato
    dd/mm/aaaa e determine se a mesma é uma data válida.
    """
    try:
        return bool(datetime.datetime.strptime(data, '%d/%m/%Y'))
    except ValueError:
        return False


def exercicio19(num: int) -> str:
    """Faça um Programa que leia um número inteiro menor que 1000
    e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros.

     Exemplo:
        326 = 3 centenas, 2 dezenas e 6 unidades
        12 = 1 dezena e 2 unidades

    Testar com:
    326, 300, 100, 320, 310,305, 301, 101, 311,
    111, 25, 20, 10, 21, 11, 1, 7 e 16
    """
    classes = ['unidade', 'dezena', 'centena']
    algarismos = []
    result = ''
    while num > 0:
        algarismos.append(num % 10)
        num //= 10
    if len(algarismos) > 3:
        raise ValueError('0 < num < 1000')

    for n, c in zip(algarismos, classes):
        result = (f'{n} {c}s ' if n > 1 else f'{n} {c} ') + result
    return result.strip()


def exercicio20(n1, n2, n3):
    """Faça um Programa para leitura de três notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e presentar:
    - A mensagem "Aprovado", se a média for maior ou igual a 7,
      com a respectiva média alcançada;
    - A mensagem "Reprovado", se a média for menor do que 7,
      com a respectiva média alcançada;
    - A mensagem "Aprovado com Distinção", se a média for igual a 10.
    """
    mensao = ['Reprovado', 'Aprovado', 'Aprovado com Distinção']
    m = sum((n1, n2, n3)) / 3
    return f'{m:.1f} - {mensao[(m >= 7) + (m == 10)]}'


def exercicio21():
    """Faça um Programa para um caixa eletrônico.

    O programa deverá perguntar ao usuário a valor do saque e depois informar
    quantas notas de cada valor serão fornecidas. As notas disponíveis serão
    as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
    de 600 reais. O programa não deve se preocupar com a quantidade de notas
    existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
    notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5
    e quatro notas de 1.
    """
    notas = [100, 50, 10, 5, 1]

    valor = float(input('Valor do saque: '))
    if valor < 10 or valor > 600:
        raise ValueError('limite por saque entre R$10 e R$600')

    def change(value) -> list:
        result = [0 for _ in range(len(notas))]
        idx = 0
        while value > 0:
            result[idx] = value // notas[idx]
            value %= notas[idx]
            idx += 1
        return result

    return ''.join(
        f'{x:.0f} nota(s) de R$ {notas[i]}, '
        for i, x in enumerate(change(valor))
        if x
    )


def exercicio22(num: int) -> str:
    """Faça um Programa que peça um número inteiro e determine
    se ele é par ou impar.

    Dica: utilize o operador módulo (resto da divisão).
    """
    # Com operador ternário
    # return 'impar' if operator.mod(num, 2) else 'par'

    return ['par', 'impar'][operator.mod(num, 2)]


def exercicio23(num: float) -> str:
    """Faça um Programa que peça um número e informe se o número é
    inteiro ou decimal.

    Dica: utilize uma função de arredondamento.

    """
    # return 'inteiro' if int(num) == num else 'decimal'
    return ['decimal', 'inteiro'][int(num) == num]


def exercicio24() -> str:
    """Faça um Programa que leia 2 números e em seguida pergunte ao
    usuário qual operação ele deseja realizar.
    O resultado da operação
    deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
    """
    pi = ['par', 'impar']
    pn = ['negativo', 'positivo']
    di = ['decimal', 'inteiro']

    def calculate(op: str, num1: float, num2: float) -> float:
        """Calculate."""
        options = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        return options.get(op)(num1, num2)

    result = calculate(
        input('operação (+-/*): '),
        float(input('número: ')),
        float(input('número: ')),
    )
    return (
        f'{result:.2f} {pi[operator.mod(int(result), 2)]}'
        f' {pn[result > 0]} {di[int(result) == result]}'
    )


def exercicio25():
    """Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

     As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre a participação
    da pessoa no crime. Se a pessoa responder positivamente a 2 questões
    ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
     5 como "Assassino".
     Caso contrário, ele será classificado como "Inocente".
    """
    status = ['Inocente', 'Suspeito', 'Cúmplice', 'Cúmplice', 'Assassino']
    perguntas = [
        'Telefonou para a vítima? ',
        'Esteve no local do crime? ',
        'Mora perto da vítima? ',
        'Devia para a vítima? ',
        'Já trabalhou com a vítima? ',
    ]
    respostas = []

    def validar_resposta(entrada: str):
        """Normalização de resposta."""
        positivas = ['sim', 'yes', 's', 'y', 'true', 'ok', '1']
        if entrada.casefold() in positivas:
            return True
        return False

    for pergunta in perguntas:
        respostas.append(validar_resposta(input(pergunta)))

    return status[max(0, sum(respostas) - 1)]


def exercicio26():
    """Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
       - até 20 litros, desconto de 3% por litro
       - acima de 20 litros, desconto de 5% por litro
    Gasolina:
       - até 20 litros, desconto de 4% por litro
       - acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
     calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço
      do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
    """
    fuels = ['A', 'AL', 'ALCOOL', 'G', 'GAZ', 'GASOLINA']

    def calculo(litragem: float = 0, combustivel: str = '') -> float:
        """Calcular valor combustivel."""
        combustivel = unidecode(combustivel.upper())
        if combustivel not in fuels:
            raise ValueError('Combustivel informado inválido.')
        if combustivel == 'A' and litragem > 20:
            return litragem * 1.9 * 95 / 100
        if combustivel == 'G' and litragem > 20:
            return litragem * 2.5 * 94 / 100
        if combustivel == 'A':
            return litragem * 1.9 * 97 / 100
        if combustivel == 'G':
            return litragem * 2.5 * 96 / 100

    #
    result = calculo(
        float(input('Quantidade de litros: ')),
        input('Qual combustível (A/G)? '))
    return f'R${result:2.2f}'
    # return list(Fuel)


def exercicio27():
    """Uma fruteira está vendendo frutas com a seguinte tabela de preços:

    Até 5 Kg
    Acima de 5 Kg
    Morango
    R$ 2,50 por Kg
    R$ 2,20 por Kg
    Maçã
    R$ 1,80 por Kg
    R$ 1,50 por Kg


    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
    ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    quantidade (em Kg) de maças adquiridas e escreva o valor a ser
    pago pelo cliente.
    """
    fruteira = {'morango': [2.5, 2.2], 'maçã': [1.8, 1.5]}
    plus_desconto = 1 - .1

    def carrinho(produtos: dict = fruteira):
        """Carrinho da frutaria."""
        car: dict[str, float] = dict()
        comprar = True
        while comprar:
            produto = input(
                f'Escolha o produto {list(produtos.keys())}: ').casefold()
            if produto not in produtos:
                print('Produto inválido, escolha novamente.')
            else:
                car[produto] = float(input('Informe a quantidade (kg):'))
            comprar = input('Acrescentar mais itens? ')[0].casefold() in ['s',
                                                                          'y']
        return car

    def calculo(car: dict[str, float]) -> float:
        """Calcular preço."""
        total = 0
        peso_total = 0
        for produto, quantia in car.items():
            peso_total += quantia
            if quantia > 5:
                total += quantia * fruteira[produto][1]
            else:
                total += quantia * fruteira[produto][0]
        if peso_total > 8 or total > 25:
            total *= plus_desconto
        return total

    return calculo(carrinho())


def exercicio28():
    """O Hipermercado Tabajara está com uma promoção de carnes que é
    imperdível. Confira:

    Até 5 Kg
    Acima de 5 Kg
    File duplo
    R$ 5,80 por Kg
    R$ 4,90 por Kg
    Alcatra
    R$ 6,80 por Kg
    R$ 5,90 por Kg
    Picanha
    R$ 7,80 por Kg
    R$ 6,90 por Kg


    Para atender a todos os clientes, cada cliente poderá levar apenas um
    dos tipos de carne da promoção, porém não há limites para a quantidade
    de carne por cliente. Se a compra for feita no cartão Tabajara o cliente
    receberá ainda um desconto de 5% sobre o total da compra.

    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
    usuário e gere um cupom fiscal, contendo as informações da compra: tipo
    e quantidade de carne, preço total, tipo de pagamento,
    valor do desconto e valor a pagar.
    """
    tipo_pag = namedtuple('Pagamento', 'tipo peso')
    pagamentos = {
        'pix': tipo_pag('pix', 1),
        'dinheiro': tipo_pag('dinheiro', 1),
        'credito': tipo_pag('crédito', 1),
        'debito': tipo_pag('débito', 1),
        'tabajara': tipo_pag('Cartão Tabajara', .95),
    }
    carnes = {
        'file duplo': [5.8, 4.9],
        'alcatra': [6.8, 5.9],
        'picanha': [7.8, 6.9],
    }

    def checking(msg: str, op: list):
        """..."""
        entrada = None
        while True:
            entrada = unidecode(e := input(f'{msg} {op}: ')).casefold()
            if entrada in op:
                break
            print(f'Opção "{e}" indisponível! Selecione novamente.')
        return entrada

    def compra():
        """Compra."""
        itens = []
        continuar = True
        forma_pagamento = ''
        forma_pagamento = checking(
            'Informe a forma de pagamento', list(pagamentos.keys()))
        carne_sel = checking('Qual carne selecionada', list(carnes.keys()))
        quantia = float(input('Quantos quilos? '))
        return forma_pagamento, carne_sel, quantia

    def ticket(*args) -> str:
        """Gera o ticket."""
        forma_pagamento, carne_sel, quantia = args
        subtotal = quantia * carnes[carne_sel][0]
        desconto = 0
        if quantia > 5:
            desconto += subtotal - quantia * carnes[carne_sel][1]
        if forma_pagamento == 'tabajara':
            desconto += subtotal * .1
        total = subtotal - desconto
        msg = (
            f'{"Hipermercado Tabajara":^40}\n'
            f'{"--"*20:^40}\n'
            'Produtos:\n'
            f'{"{:<5}Kg {:<10} ......... {:>10}"}\n'
            f'{"--"*20:^40}\n'
            f'{"Tipo de pagamento: {:>20}"}\n'
            f'{"Valor do desconto: {:>20}"}\n'
            f'{"Valor Final: {:>26}"}\n'
        )
        return msg.format(
            quantia,
            carne_sel,
            f'R$ {subtotal:.2f}',
            pagamentos[forma_pagamento].tipo,
            f'R$ {desconto:.2f}',
            f'R$ {total:.2f}',
        )

    return ticket(*compra())
