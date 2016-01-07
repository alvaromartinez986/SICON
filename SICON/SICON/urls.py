from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *
from administrador.views import *




urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^dropdown_modelo',cargar_modelos),
    url(r'^login$',iniciar_sesion),
    url(r'^logout',cerrar_sesion),

    url(r'^',include('administrador.urls')),


)




