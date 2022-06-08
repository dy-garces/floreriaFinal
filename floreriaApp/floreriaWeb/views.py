<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render, redirect
from floreriaWeb.Carrito import Carrito
from .models import Producto
from .forms import FormularioProducto,CustomUserCreationForm
from django.contrib.auth import authenticate, login
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

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='home')
        data["form"] = formulario    

    return render(request,"registration/registro.html",data)


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

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def guardar(request, total):
    usuario = request.user
    total = total(request)
    carrito = Carrito(request)
    tot = tot["total_carrito"]

def carrito(request):
    return render(request,"floreriaWeb/carrito.html")
=======
from django.shortcuts import get_object_or_404, render, redirect
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

def mostrar_producto(request,id):
    
    producto = get_object_or_404(Producto, id_producto=id)
    
    data = {
        'producto' : producto
    }
    
    return render(request,"floreriaWeb/mostrar_producto.html",data)

def registro(request):
    return render(request,"registration/registro.html")

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
 
>>>>>>> nestor2
