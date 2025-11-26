from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ReceitaForm
from .models import Receita


# Create your views here.
def receitas(request: HttpRequest) -> HttpResponse:
    """Receitas."""
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context=context)


def detalhes_receita(request: HttpRequest, id_receita: int) -> HttpResponse:
    """Detalhes da receita."""
    receita = Receita.objects.get(id=id_receita)
    context = {'receita': receita}

    return render(request, template_name='detalhes_receita.html', context=context)

def nova_receita(request: HttpRequest) -> HttpResponse:
    """Nova receita."""
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('receitas')
    form = ReceitaForm()
    return render(request, 'nova_receita.html', context={'form': form})

