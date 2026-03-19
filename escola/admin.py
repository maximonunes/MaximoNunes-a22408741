from django.contrib import admin
from .models import Escola


class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "endereco")   # mostra na lista
    ordering = ("nome",)                  # ordena por nome
    search_fields = ("nome", "endereco")  # pesquisa por nome e endereço


admin.site.register(Escola, EscolaAdmin)
# Register your models here.
