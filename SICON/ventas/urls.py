from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^ventas/cotizacion/vehiculos',cotizar_vehiculos, name='cotizacion_vehiculos')

)