__author__ = 'Fernando'
from django.conf.urls import patterns, include, url
from .views import *
from .views_vehiculos import *

urlpatterns = patterns('',
    url(r'^crearvn',crear_vehiculo_nuevo),
    url(r'^editarvn/(\d+)$',editar_vehiculo_nuevo),
    url(r'^listarvn',listar_vehiculos_nuevos),
    url(r'^eliminarvn/(\d+)$',eliminar_vehiculo_nuevo),
    url(r'^crearvu',crear_vehiculo_usado),
    url(r'^editarvu/(\d+)$',editar_vehiculo_usado),
    url(r'^listarvu',listar_vehiculos_usados),
    url(r'^eliminarvu/(\d+)$',eliminar_vehiculo_usado),

)
