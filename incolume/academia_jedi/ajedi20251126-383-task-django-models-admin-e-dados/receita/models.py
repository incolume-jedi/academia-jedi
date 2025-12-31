from django.db import models


# Create your models here.
class Categoria(models.Model):
    """Class Categoria."""

    nome = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.nome


class Receita(models.Model):
    """Class Receita."""

    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    data_criado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo
