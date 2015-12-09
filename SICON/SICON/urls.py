from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *
from administrador.views import *




urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^login$',iniciar_sesion),
    url(r'^logout',cerrar_sesion),
    url(r'^repuestos-editar/(\d+)$',editar_repuesto),
    url(r'^repuestos/crear',crear_repuesto),
    url(r'^repuestos/',listar_repuestos),
    url(r'^repuestos-inventario/(\d+)$',inventario),
    url(r'^vehiculos_nuevos/',include('administrador.urls')),
    url(r'^vehiculos_usados/',include('administrador.urls')),
    url(r'^sucursales/',include('administrador.urls')),
    url(r'^repuestos/',listar),
    url(r'^login$',iniciar_sesion),
    url(r'^logout',cerrar_sesion),
    url(r'^empleado/crear', crear_empleado),
    url(r'^empleado/listar', listar_empleado),
    url(r'^empleado/editar/(\d+)$', editar_empleado)
)
