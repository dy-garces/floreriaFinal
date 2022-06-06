from unicodedata import name
from django.urls import path
from floreriaWeb.views import home,flores,plantas,arboles,maceteros,jardineria,contacto,quienesSomos,mostrar_producto,registro,FormProducto


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
    path("FormProducto/",FormProducto,name="FormProducto")
]

