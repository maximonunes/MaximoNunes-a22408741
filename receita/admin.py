from django.contrib import admin
from .models import Receita, Ingrediente

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tempo_preparo")
    ordering = ("nome",)
    search_fields = ("nome",)
    list_filter = ()  # ou remove esta linha

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)





admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
# Register your models here.
