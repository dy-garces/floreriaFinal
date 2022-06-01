from django.shortcuts import render
from .models import Producto
# Create your views here.

def home(request):
    
    return render(request,"floreriaWeb/home.html")
def flores(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos,
    }
    return render(request,'floreriaWeb/flores.html',contexto)

def plantas(request):

    return render(request,'floreriaWeb/plantas.html')

def arboles(request):

    return render(request,'floreriaWeb/arboles.html')

def maceteros(request):

    return render(request,"floreriaWeb/maceteros.html")

def jardineria(request):

    return render(request,"floreriaWeb/jardineria.html")

def contacto(request):

    return render(request,"floreriaWeb/contacto.html")

def quienesSomos(request):

    return render(request,"floreriaWeb/quienesSomos.html")