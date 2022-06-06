from django.shortcuts import redirect, render
from .models import Producto
from .forms import FormularioProducto
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

def FormProducto(request):
    form=FormularioProducto(request.POST or None)
    contexto={
        "form":FormularioProducto
    }
    
    if request.method=="POST":
        form=FormularioProducto(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="home")
    return render(request,"floreriaWeb/FormularioProducto.html", contexto)
