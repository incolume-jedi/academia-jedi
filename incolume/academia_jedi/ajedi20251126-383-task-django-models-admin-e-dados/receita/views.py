from django.shortcuts import render
from django.http import HttpRequest
from .models import Receita


# Create your views here.
def receitas(request: HttpRequest):
    """Receitas."""
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context=context)


def detalhes_receita(request: HttpRequest, id_receita: int):
    """Detalhes da receita."""
    receita = Receita.objects.get(id=id_receita)
    context = {'receita': receita}

    return render(request, template_name='detalhes_receita.html', context=context)
