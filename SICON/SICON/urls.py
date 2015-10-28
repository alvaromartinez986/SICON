from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from django.shortcuts import render

urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^a',listar),
)
