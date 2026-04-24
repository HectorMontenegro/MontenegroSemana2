from django.contrib import admin
<<<<<<< HEAD
from .models import Empleado, Encomienda, HistorialEstado


@admin.register(Encomienda)
class EncomiendaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'remitente', 'destinatario', 'ruta', 'estado', 'fecha_registro')
    list_filter = ('estado', 'ruta')
    search_fields = ('codigo', 'remitente__nro_doc', 'destinatario__nro_doc')
    readonly_fields = ('fecha_registro',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'apellidos', 'nombres', 'cargo', 'estado')
    search_fields = ('codigo', 'apellidos', 'nombres')
    filter_horizontal = ('rutas_asignadas',)


@admin.register(HistorialEstado)
class HistorialEstadoAdmin(admin.ModelAdmin):
    list_display = ('encomienda', 'estado_anterior', 'estado_nuevo', 'empleado', 'fecha_cambio')
    readonly_fields = ('fecha_cambio',)
=======

# Register your models here.
from django.contrib import admin
from .models import Encomienda

@admin.register(Encomienda)
class EncomiendaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'peso_kg', 'estado', 'fecha_envio')
    list_filter = ('estado',)
    search_fields = ('codigo', 'descripcion')
>>>>>>> bdce5c42d12aef25eec1cb6eb0b53bcb56addb1f
