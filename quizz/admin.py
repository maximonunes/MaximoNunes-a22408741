from django.contrib import admin
from .models import Quizz


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("texto",)
    ordering = ("texto",)
    search_fields = ("texto",)


admin.site.register(Quizz, PerguntaAdmin)
# Register your models here.
