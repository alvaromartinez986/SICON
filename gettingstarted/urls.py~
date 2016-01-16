from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *
from administrador.views import *




urlpatterns = patterns('',
    url(r'^index',index),
    url(r'^dropdown_modelo',cargar_modelos),
    url(r'^login',iniciar_sesion),
    url(r'^logout',cerrar_sesion),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^',include('administrador.urls')),
    url(r'^',include('ventas.urls')),


)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

