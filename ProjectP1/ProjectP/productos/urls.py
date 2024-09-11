from django.urls import path
from .views import ProductoFormView  # Importa la vista que renderiza el formulario, no el formulario mismo

urlpatterns = [
    # Aquí se debe usar la vista basada en clases ProductoFormView, no ProductoForm
    path('agregar/', ProductoFormView.as_view(), name='add_product'),
]
