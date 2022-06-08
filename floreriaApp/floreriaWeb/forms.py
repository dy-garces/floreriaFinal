from django import forms
from django.db.models import fields
from .models import PerfilUsuario, Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ["nombre", "precio", "descripcion", "imgen", "categoria"]
        fields= '__all__'
        
class frmPerfilUsuario(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields=["rut","nombre","apellido","direccion"]