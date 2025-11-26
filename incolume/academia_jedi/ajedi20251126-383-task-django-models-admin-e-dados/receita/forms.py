from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    """Class ReceitaForm."""
    class Meta:
        model = Receita
        # fields = '__all__'
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']

        def clean_titulo(self):
            """Validation."""
            titulo = self.cleaned_data['titulo'].strip()

            if len(titulo) < 3:
                msg = 'O título precisa ter ao menos 3 characteres.'
                raise forms.ValidationError(msg)
