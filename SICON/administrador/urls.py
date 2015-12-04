__author__ = 'Fernando'
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^listar',listar_sucursales),
	url(r'^crear',crear_sucursal),
	url(r'^cargar_ciudades', cargar_ciudades),
	url(r'^eliminar/(\d+)$',eliminar_sucursal),
	url(r'^editar/(\d+)$',editar_sucursal),
)
