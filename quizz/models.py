from django.db import models

class Quizz(models.Model):
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto
# Create your models here.
