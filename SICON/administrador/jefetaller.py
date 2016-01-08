__author__ = 'JuanDiego'
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from .empleado import *


class JefeTaller(User, Empleado):
    class Meta:
        '''permissions = (
            # Permission identifier     human-readable permission name
            ("anadir_calificaciones", "Puede calificar cursos"),
            ("editar_datos_personales", "Puede editar sus propios datos"),
            ("terminar_datos_mt", "Terminar datos lab y acad mt"),
        #)'''

    def __str__(self):
        return self.get_full_name()
