from django.conf.urls import patterns, include, url
from .views import *



urlpatterns = patterns('',
    url(r'^reportes/inventario_repuestos', mas_movimientos, name='inventario_repuestos'),
)



