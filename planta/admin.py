from django.contrib import admin

from .models import Trabajador, Categoria, Producto, Produccion

# Register your models here.

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'cedula', 'nombre', 'apellido', 'correo', 'nombreCompleto')
    search_fields = ['nombre', 'cedula']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'desc')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ficha_tecnica', 'costo', 'categoria', 'color', 'descripcionCategoria')
    search_fields = ['nombre', 'categoria__nombre', 'categoria__desc']
    list_filter = ['categoria']
    #list_editable = ['color']
    
    def descripcionCategoria(self, obj):
        return obj.categoria.desc

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabajador', 'producto', 'cantidad', 'fecha_creacion')