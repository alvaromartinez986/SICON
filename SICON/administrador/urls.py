__author__ = 'Fernando'
from django.conf.urls import patterns, include, url
from .views import *
from .views_vehiculos import *

urlpatterns = patterns('',
    url(r'^crearvn',crear_vehiculo_nuevo),
    url(r'^editarvn/(\d+)$',editar_vehiculo_nuevo),
    url(r'^listarvn',listar_vehiculos_nuevos),
    url(r'^crearvu',crear_vehiculo_usado),

)
