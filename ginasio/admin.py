from django.contrib import admin
from .models import Cliente, Treinador, Sessao

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "email", "data_registo")  # campos existentes
    ordering = ("nome_completo",)                                # campo existente
    search_fields = ("nome_completo", "email")                  # campos existentes

admin.site.register(Cliente, ClienteAdmin)
