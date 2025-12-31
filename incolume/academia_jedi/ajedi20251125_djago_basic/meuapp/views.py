from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from pytz import timezone

# Create your views here.
estoque_produtos = {
    1: 'produto 01',
    2: 'produto 02',
    3: 'produto 03',
    4: 'produto 04',
    5: 'produto 05',
    6: 'produto 06',
    7: 'produto 07',
}


def home(request: HttpRequest, nome: str = '') -> HttpResponse:
    """Home."""
    nome = nome or 'Visitante'
    return render(request, 'home.html', {'nome': nome})


def timestamp(request: HttpRequest) -> HttpResponse:
    """Timestamp."""
    hora_atual = datetime.now(tz=timezone('America/Sao_Paulo'))

    return HttpResponse(f'São {hora_atual}')


def saudacao(request: HttpRequest, nome: str = '') -> HttpResponse:
    """Saudação."""
    nome = nome.capitalize() or 'Visitante'
    msg = f'Olá {nome}, Seja bem vind{"a" if nome.endswith("a") else "o"}!'

    return HttpResponse(msg)


def produto(request: HttpRequest, id_produto: int) -> HttpResponse:
    """Produto."""
    produto = estoque_produtos.get(id_produto, 'Produto não encontrado.')
    return HttpResponse(f'Descrição: {produto}')


def produtos(request: HttpRequest) -> HttpResponse:
    """Produtos."""
    return render(
        request,
        'produtos.html',
        {'produtos': estoque_produtos.values()},
    )


def index(request: HttpRequest) -> HttpResponse:
    """Index."""
    return render(
        request,
        'index.html',
        {'title': 'Index page', 'head': 'Index Page'},
    )
