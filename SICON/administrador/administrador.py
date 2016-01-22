from django.contrib import admin

from django.contrib.admin import AdminSite

from .models import Empleado, Gerente, JefeTaller, Repuesto, Sucursal, SuperAdmin, Vehiculo, VehiculoNuevo
from .models import Vendedor, VehiculoUsado

class MyAdminSite(AdminSite):
    site_header = 'Administrador de Django'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Empleado)
admin_site.register(Gerente)
admin_site.register(JefeTaller)
admin_site.register(Repuesto)
admin_site.register(SuperAdmin)
admin_site.register(Vehiculo)
admin_site.register(Sucursal)
admin_site.register(VehiculoNuevo)
admin_site.register(VehiculoUsado)
admin_site.register(Vendedor)
