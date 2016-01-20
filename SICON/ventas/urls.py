from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^ventas/cotizacion/cliente',id_cliente, name='id_cliente'),
	url(r'^ventas/clientes/(\d+)$',gestionar_cliente, name='clientes'),
	url(r'^ventas/cotizacion/vehiculos/(\d+)$',cotizar_vehiculos, name='cotizar_vehiculos'),

	#  venta
	url(r'^ventas/venta/cliente',id_cliente_venta, name='id_cliente_venta'),
	url(r'^ventas/cliente_venta/(\d+)$',gestionar_cliente_venta, name='clientes_venta'),
	url(r'^ventas/venta/vehiculos/(\d+)$',venta_vehiculos, name='venta_vehiculos'),
	url(r'^ventas/venta/final',venta_final, name='venta_final'),
	url(r'^ventas/venta/genpdf',registrar_venta, name='registrar_venta'),

)