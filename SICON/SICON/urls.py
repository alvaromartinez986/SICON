from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render
from django.contrib import admin
from .views import *
from SICON.administrador.views import *
from SICON.SICON import settings




urlpatterns = patterns('',
    url(r'^indexAdmin',index_admin),
    url(r'^login',iniciar_sesion),
    url(r'^dropdown_modelo',cargar_modelos),
    url(r'^logout',cerrar_sesion),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^',include('SICON.administrador.urls')),
    url(r'^',include('SICON.ventas.urls')),
    url(r'^',index),


)
#estas lineas se descomentan cuando se trabaje en heroku master
# urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )
#
