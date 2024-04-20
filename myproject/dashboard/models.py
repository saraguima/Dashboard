from django.db import models
from .forms import formularios_upload
from datetime import datetime

class formularios_upload (models.Model):
    mes = models.CharField(max_length=20)
    ano = models.IntegerField()
    valor_vendas = models.DecimalField(max_digits=10, decimal_places=2)
    