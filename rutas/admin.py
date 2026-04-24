from django.contrib import admin
<<<<<<< HEAD
from .models import Ruta


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'origen', 'destino', 'precio_base', 'dias_entrega', 'estado')
    list_filter = ('estado',)
    search_fields = ('codigo', 'origen', 'destino')
=======

# Register your models here.
>>>>>>> bdce5c42d12aef25eec1cb6eb0b53bcb56addb1f
