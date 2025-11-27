from django.db import models

from django.contrib.auth.models import User

class OrdemServico(models.Model):
    cliente = models.CharField(max_length=70)
    telefone = models.CharField(max_length=20, unique=True)
    moto = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    problema_relatado = models.TextField(max_length=500)
    servico_executado = models.TextField(max_length=500)
    mecanico_responsavel = models.CharField(max_length=30)
    atendente_responsalvel = models.ForeignKey(User, on_delete=models.SET_NULL, max_length=50, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'OS {self.id} do cliente {self.cliente}'