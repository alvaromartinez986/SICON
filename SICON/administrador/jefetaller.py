__author__ = 'JuanDiego'
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from .empleado import *


class JefeTaller(User, Empleado):
    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_Jefe_Taller",       "Se permite editar, activar , desactivar" ),
        )

    def __str__(self):
        return self.get_full_name()
