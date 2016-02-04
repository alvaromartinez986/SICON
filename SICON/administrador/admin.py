from django.contrib import admin
from .models import Empleado, Gerente, JefeTaller, Repuesto, Sucursal, SuperAdmin, Vehiculo, VehiculoNuevo,Marca
from .models import Vendedor, VehiculoUsado
admin.site.register(Empleado)
admin.site.register(Gerente)
admin.site.register(JefeTaller)
admin.site.register(Repuesto)
admin.site.register(SuperAdmin)
admin.site.register(Vehiculo)
admin.site.register(Sucursal)
admin.site.register(VehiculoNuevo)
admin.site.register(VehiculoUsado)
admin.site.register(Vendedor)
admin.site.register(Marca)