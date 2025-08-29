from django.contrib import admin
from .models import Venda

admin.site.register(Venda)

class VendaAdmin(admin.ModelAdmin):
    list_display = ("mes", "ano", "valor_vendas")
    list_filter = ("ano", "mes")
    search_fields = ("mes",)