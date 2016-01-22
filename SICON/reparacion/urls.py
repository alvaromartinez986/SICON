from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *




urlpatterns = patterns('',
    url(r'^reparacion/listar_ordenes', listar_ordenes, name='listar_ordenes'),
    url(r'^reparacion/crear_orden', crear_orden, name='crear_orden'),
    url(r'^reparacion/estado_orden/([^/]+)$',devuelve_estado, name='devuelve_estado'),


)




