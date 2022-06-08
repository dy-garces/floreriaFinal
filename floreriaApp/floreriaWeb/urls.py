from unicodedata import name
from django.urls import path
from floreriaWeb.views import home,flores, modificarproducto,plantas,arboles,maceteros,jardineria,contacto,quienesSomos,mostrar_producto,registro,FormProducto,productoslistados,modificarproducto,eliminarproducto


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
    path("FormProducto/",FormProducto,name="FormProducto"),
    path("productoslistados/",productoslistados, name="productoslistados"),
    path("modificarproducto/<id_producto>/", modificarproducto, name="modificarproducto"),
    path("eliminarproducto/<id_producto>",eliminarproducto, name="eliminarproducto"),
]

