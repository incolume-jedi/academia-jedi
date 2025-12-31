from typing import ClassVar

from django.contrib import admin

from .models import Categoria, Receita


class ReceitasDisplay(admin.ModelAdmin):
    """Class ReceitaDisplay."""

    list_display: ClassVar[list[str]] = ['titulo', 'categoria', 'data_criado']
    search_fields: ClassVar[list[str]] = ['titulo', 'categoria']
    list_filter: ClassVar[list[str]] = ['categoria', 'data_criado']


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Receita, ReceitasDisplay)
