from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    email = models.EmailField(verbose_name="Email del cliente")

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    fecha = models.DateField(verbose_name="Fecha del pedido")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total del pedido")



def __str__(self):
    return self.nombre