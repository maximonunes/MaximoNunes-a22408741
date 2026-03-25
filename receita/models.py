from django.db import models

<<<<<<< HEAD

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
=======
# Create your models here.
class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    favoritada_por = models.ManyToManyField(Utilizador, blank=True)

    def __str__(self):
        return self.titulo
# Create your models here.
>>>>>>> 9e06b5ef643195a75be1072c1b62f152cacf9ffe
