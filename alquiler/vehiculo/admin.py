from django.contrib import admin

from .models import Vehiculo
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa','marca','modelo')

# Register your models here.
admin.site.register(Vehiculo, VehiculoAdmin)