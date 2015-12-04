from django.db import models
from django.utils.encoding import smart_unicode
from .empleado import *
__author__='nelson'

class Usuarios(Empleado):
    id_empleado = mmodels.ForeignKey(Empleado)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)