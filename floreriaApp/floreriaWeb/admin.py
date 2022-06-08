from django.contrib import admin

from floreriaWeb.models import Categoria,Producto,Region,Comuna,Vendedor,Cliente,Venta,Forma_Pago,Seguimiento_Compra,Detalle_Venta,Estado_subcripcion,Subcripcion

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Forma_Pago)
admin.site.register(Seguimiento_Compra)
admin.site.register(Detalle_Venta)
admin.site.register(Estado_subcripcion)
admin.site.register(Subcripcion)