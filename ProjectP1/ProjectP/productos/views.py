from django.views import generic
from .forms import ProductoForm  

# Vista basada en clases que maneja el formulario
class ProductoFormView(generic.FormView):
    template_name = 'form.html'  # Plantilla HTML que renderiza el formulario
    form_class = ProductoForm