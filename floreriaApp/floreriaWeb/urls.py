from unicodedata import name
from django.urls import path
<<<<<<< HEAD
from floreriaWeb.views import home,flores,plantas,arboles,maceteros,jardineria,contacto,quienesSomos,mostrar_producto,registro,FormProducto,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito,carrito
=======
from floreriaWeb.views import FormProducto,home,flores,plantas,arboles,maceteros,jardineria,contacto,quienesSomos,mostrar_producto,registro
>>>>>>> nestor2


urlpatterns = [
    path('',home,name="home"),
    path('flores/',flores,name="flores"),
    path('plantas/',plantas,name="plantas"),
    path('arboles/',arboles,name="arboles"),
    path('maceteros',maceteros,name="maceteros"),
    path('jardineria/',jardineria,name="jardineria"),
    path('contacto/',contacto,name="contacto"),
    path('quienesSomos',quienesSomos,name="quienesSomos"),
    path('mostrar_producto/<id>',mostrar_producto, name="mostrar_producto"),
    path('registro',registro, name="registro"),
<<<<<<< HEAD
    path("FormProducto/",FormProducto,name="FormProducto"),
    
    path('agregar/<int:producto_id>/', agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('carrito/',carrito,name="carrito"),
=======
    path("FormProducto/",FormProducto,name="FormProducto")
>>>>>>> nestor2
]

