from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    tempo_preparo = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.tempo_preparo} min)"
# Create your models here.
