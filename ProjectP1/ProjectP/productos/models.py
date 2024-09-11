from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción del producto")
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio del producto"
    )
    photo = models.ImageField(upload_to="productos", null=True, blank=True , verbose_name="Foto del producto")
    disponible = models.BooleanField(default=True, verbose_name="Producto disponible")



def __str__(self):
    return self.nombre
