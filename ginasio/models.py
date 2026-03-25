from django.db import models

class Treinador(models.Model):
    nome_completo = models.CharField(max_length=100)
    area_especializacao = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"PT: {self.nome_completo}"


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_registo = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo


class Sessao(models.Model):
    treinador = models.ForeignKey(
        Treinador,
        on_delete=models.CASCADE,
        related_name='sessoes'
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    data_sessao = models.DateField()
    hora_sessao = models.TimeField()

    class Meta:
        unique_together = ('treinador', 'data_sessao', 'hora_sessao')

    def __str__(self):
        return f"{self.cliente} com {self.treinador} em {self.data_sessao} às {self.hora_sessao}"
