from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from administrador.views import *




urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^dropdown_modelo',cargar_modelos),
    url(r'^repuestos-editar/(\d+)$',editar_repuesto),
    url(r'^repuestos-editar/(\d+)$',editar_repuesto),
    url(r'^repuestos/crear',crear_repuesto),
    url(r'^repuestos/',listar_repuestos),
    url(r'^repuestos-inventario/(\d+)$',inventario),
    url(r'^repuestos-eliminar/(\d+)$',eliminar_repuesto),

)




