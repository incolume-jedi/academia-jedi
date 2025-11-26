from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    """Class ReceitaForm."""
    class Meta:
        model = Receita
        # fields = '__all__'
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']
