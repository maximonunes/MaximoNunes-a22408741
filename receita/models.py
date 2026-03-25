from django.db import models

from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    tempo_preparo = models.PositiveIntegerField()
    ingredientes = models.ManyToManyField(
        Ingrediente,
        related_name='receitas'
    )

    def __str__(self):
        return f"{self.nome} ({self.tempo_preparo} min)"