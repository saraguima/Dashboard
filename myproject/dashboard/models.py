from django.db import models

class Venda(models.Model):
    mes = models.CharField(max_length=20)
    ano = models.IntegerField()
    valor_vendas = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.mes}/{self.ano} - {self.valor_vendas}"