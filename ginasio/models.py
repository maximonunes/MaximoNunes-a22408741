from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    plano = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.plano}"
# Create your models here.
