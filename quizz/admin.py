from django.contrib import admin
from .models import Pergunta


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("texto",)
    ordering = ("texto",)
    search_fields = ("texto",)


admin.site.register(Pergunta, PerguntaAdmin)
# Register your models here.
