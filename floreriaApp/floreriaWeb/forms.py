from django import forms
from django.db.models import fields
from .models import Producto

class RegistrarProducto(forms.ModelForm):
    
    class Meta:
        model = Producto
        
        fields = '__all__'