from django.contrib import admin
<<<<<<< HEAD
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nro_doc', 'tipo_doc', 'apellidos', 'nombres', 'telefono', 'estado')
    list_filter = ('tipo_doc', 'estado')
    search_fields = ('nro_doc', 'apellidos', 'nombres')
=======

# Register your models here.
>>>>>>> bdce5c42d12aef25eec1cb6eb0b53bcb56addb1f
