from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^ventas/cotizacion/cliente',id_cliente, name='id_cliente'),
	url(r'^ventas/clientes/(\d+)$',gestionar_cliente, name='clientes')
)