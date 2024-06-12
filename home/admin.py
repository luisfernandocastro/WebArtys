from django.contrib import admin

# Register your models here.

from .models import * # Se  importan todas las tablas del modelo de base de datos del archivo models.py 


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Comprador)
admin.site.register(carrito_compras)
admin.site.register(Perfilusuario)