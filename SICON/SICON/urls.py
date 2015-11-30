from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render



urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^vehiculos_nuevos/',include('administrador.urls')),
    url(r'^vehiculos_usados/',include('administrador.urls')),
    url(r'^sucursales/',include('administrador.urls')),
    url(r'^repuestos/',listar),
)




