from django import forms
from django.db.models import fields
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ["nombre", "precio", "descripcion", "imgen", "categoria"]
        fields= '__all__'