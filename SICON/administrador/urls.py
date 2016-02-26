__author__ = 'Fernando'
from django.conf.urls import patterns, include, url
from .views import *
from .views_vehiculos import *

urlpatterns = patterns('',
    url(r'^vehiculos_nuevos/crearvn',crear_vehiculo_nuevo),
    url(r'^vehiculos_nuevos/editarvn/(\d+)$',editar_vehiculo_nuevo),
    url(r'^vehiculos_nuevos/listarvn',listar_vehiculos_nuevos, name='listar_vehiculos_nuevos'),
    url(r'^vehiculos_nuevos/eliminarvn/(\d+)$',eliminar_vehiculo_nuevo),
    url(r'^vehiculos_usados/crearvu',crear_vehiculo_usado),
    url(r'^vehiculos_usados/editarvu/(\d+)$',editar_vehiculo_usado),
    url(r'^vehiculos_usados/listarvu',listar_vehiculos_usados, name='listar_vehiculos_usados'),
    url(r'^vehiculos_usados/eliminarvu/(\d+)$',eliminar_vehiculo_usado),

	url(r'^sucursales/listar',listar_sucursales, name= 'listar_sucursales'),
	url(r'^sucursales/crear',crear_sucursal, name='sucursales_crear'),
	url(r'^sucursales/cargar_ciudades', cargar_ciudades),
	url(r'^sucursales/eliminar/(\d+)$',eliminar_sucursal, name='sucursales_eliminar'),
	url(r'^sucursales/editar/(\d+)$',editar_sucursal, name='sucursales_editar'),

    url(r'^repuestos-editar/(\d+)$',editar_repuesto,name='editar_repuesto'),
    url(r'^repuestos/crear',crear_repuesto,name='crear_repuesto'),
    url(r'^repuestos/',listar_repuestos, name='listar_repuestos'),
    url(r'^repuestos-inventario/(\d+)$',inventario,name='inventario_repuesto'),
    url(r'^repuestos-eliminar/(\d+)$',eliminar_repuesto,name='eliminar_repuesto'),

    url(r'^empleado/crear_empleado', crear_empleado, name='crear_empleado'),
    url(r'^empleado/listar_empleados', listar_empleado, name='listar_empleados'),
    url(r'^empleado/editar_empleado/(\d+)$', editar_empleado),
    url(r'^empleado/eliminar_empleado/(\d+)$', eliminar_empleado),


    url(r'^reporte_repuestos', reporte_repuestos, name='reporte_repuestos'),
    url(r'^repuestos_movimientos', data_repuestos, name='data_repuestos'),
    url(r'^reportes', ver_reportes, name='reportes')

)
