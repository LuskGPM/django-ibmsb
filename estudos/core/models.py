from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, default='')
    ativo = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True, blank=True)
    
class Fatura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)
