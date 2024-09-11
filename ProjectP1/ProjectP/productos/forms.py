from django import forms
from .models import Producto

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del producto")
    descripcion = forms.CharField(
        widget=forms.Textarea, label="Descripción del producto"
    )
    precio = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio del producto"
    )
    photo = forms.ImageField(required=False, label="Foto del producto")
    disponible = forms.BooleanField(required=True, label="Producto disponible")

    # Función para guardar los datos del formulario
    def save(self):
        Producto.objects.create(
            nombre=self.cleaned_data["nombre"],
            descripcion=self.cleaned_data["descripcion"],
            precio=self.cleaned_data["precio"],
            photo=self.cleaned_data["photo"],
            disponible=self.cleaned_data["disponible"],
        )
