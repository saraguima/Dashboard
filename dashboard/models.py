from django.db import models
from datetime import datetime

class vendasmes (models.Model):
    mes = models.CharField(max_length=20)
    ano = models.IntegerField()
    valor_vendas = models.DecimalField(max_digits=10, decimal_places=2)
    