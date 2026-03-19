from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
# Create your models here.
