from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *




urlpatterns = patterns('',
    url(r'^reparacion/listar_ordenes', listar_ordenes, name='listar_ordenes'),
    url(r'^reparacion/crear_orden', crear_orden, name='crear_orden'),
    url(r'^reparacion/estado_orden/([^/]+)$', devuelve_estado, name='devuelve_estado'),
    url(r'^reparacion/eliminar_orden/(\d+)$', eliminar_orden, name='eliminar_orden'),
    url(r'^reparacion/editar_orden/(\d+)$', editar_orden, name='editar_orden'),
    url(r'^reparacion/finalizar_orden/(\d+)$', finalizar_orden, name='finalizar_orden'),
    url(r'^reparacion/editar_detalle_repuesto/(\d+)$', editar_detalle_repuesto, name='editar_detalle_repuesto'),
    # url(r'^reparacion/crear_detalle_repuesto/(\d+)$', crear_detalle_repuesto, name='crear_detalle_repuesto'),


)




