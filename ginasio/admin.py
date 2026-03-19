from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "plano")
    ordering = ("nome",)
    search_fields = ("nome", "plano")


admin.site.register(Cliente, ClienteAdmin)
# Register your models here.
