from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from administrador.views import *




urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^repuestos-editar/(\d+)$',editar_repuesto),
    url(r'^repuestos/crear',crear_repuesto),
    url(r'^repuestos/',listar_repuestos),
    url(r'^login$',iniciar_sesion),
    url(r'^logout',cerrar_sesion),
    url(r'^empleado/crear', crear_empleado),
    url(r'^empleado/listar', listar_empleado),
    url(r'^empleado/editar/(\d+)$', editar_empleado)
)
