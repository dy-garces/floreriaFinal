import re
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from .models import PerfilUsuario, Producto
from .forms import FormularioProducto, frmPerfilUsuario
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    
    return render(request,"floreriaWeb/home.html")

def flores(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'floreriaWeb/flores.html',contexto)

def plantas(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }

    return render(request,'floreriaWeb/plantas.html',contexto)

def arboles(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'floreriaWeb/arboles.html',contexto)

def maceteros(request):
    
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }

    return render(request,"floreriaWeb/maceteros.html",contexto)

def jardineria(request):
    
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }

    return render(request,"floreriaWeb/jardineria.html",contexto)

def contacto(request):

    return render(request,"floreriaWeb/contacto.html")

def quienesSomos(request):

    return render(request,"floreriaWeb/quienesSomos.html")

def mostrar_producto(request,id):
    
    producto = get_object_or_404(Producto, id_producto=id)
    
    data = {
        'producto' : producto
    }
    
    return render(request,"floreriaWeb/mostrar_producto.html",data)

def FormProducto(request):
    form=FormularioProducto(request.POST or None)
    contexto={
        "form":FormularioProducto
    }
    
    if request.method=="POST":
        form=FormularioProducto(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="home")
    return render(request,"floreriaWeb/FormularioProducto.html", contexto)
 
 ########################################################################## Perfil usuario
def registro(request):
    form=UserCreationForm(request.POST or None)
    contexto={
        "frm":form
    }
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data("username"),password=form.cleaned_data("password1"))
            login(request,credenciales)
            return redirect(to="perfilusuario.html")
        
    return render(request,"registration/registro.html",contexto)


def perfilusuario(request):
    form=frmPerfilUsuario(request.POST or None)
    contexto={
        "frm":form
    }
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            perfil=PerfilUsuario()
            perfil.rut=datos.get("rut")
            perfil.nombre=datos.get("nombre")
            perfil.apellido=datos.get("apellido")
            perfil.direccion=datos.get("direccion")
            perfil.nombre_usuario=request.user.username
            perfil.save()         
            return redirect(to="home")
        
    return render(request,"floreriaWeb/perfilusuario.html",contexto)

def cabiarpassword(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "frm":form
    }
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data("username"),password=form.cleaned_data("password1"))
            login(request,credenciales)
            return redirect(to="perfilusuario.html")
        
    return render(request,"registration/registro.html",contexto)