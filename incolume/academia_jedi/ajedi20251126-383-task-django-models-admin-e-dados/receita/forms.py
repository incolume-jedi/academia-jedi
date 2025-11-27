from typing import ClassVar
from django import forms

from .models import Receita


class ReceitaForm(forms.ModelForm):
    """Class ReceitaForm."""
    class Meta:
        """Meta class."""
        model = Receita
        # fields = '__all__'
        fields: ClassVar[list[str]] = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']

        def clean_titulo(self):
            """Validation."""
            titulo = self.cleaned_data['titulo'].strip()

            if len(titulo) < 3:
                msg = 'O título precisa ter ao menos 3 characteres.'
                raise forms.ValidationError(msg)
            return titulo
