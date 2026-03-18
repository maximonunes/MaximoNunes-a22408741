from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade")      # mostra estes campos na lista
    ordering = ("nome", "idade")          # ordena primeiro pelo nome
    search_fields = ("nome",)             # ativa a pesquisa por nome
    
admin.site.register(Pessoa)

# Register your models here.
