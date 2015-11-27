__author__ = 'Nelson'
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^listar',listar_empleado),
	url(r'^crear',crear_empleado),
)
