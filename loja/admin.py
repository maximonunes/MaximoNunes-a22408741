from django.contrib import admin
from .models import Produto, Categoria as CategoriaProduto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock", "disponivel", "categoria")
    ordering = ("nome",)
    search_fields = ("nome",)
    list_filter = ("disponivel", "categoria")


class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(CategoriaProduto, CategoriaProdutoAdmin)
