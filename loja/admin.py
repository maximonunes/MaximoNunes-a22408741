from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    ordering = ("nome",)
    search_fields = ("nome",)


admin.site.register(Produto, ProdutoAdmin)

# Register your models here.
