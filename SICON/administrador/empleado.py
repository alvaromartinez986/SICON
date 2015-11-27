from django.db import models
from django.utils.encoding import smart_unicode

__author__ = 'nelson'

class Empleado(models.Model):
    no_documento =      models.IntegerField(unique=True)
    nombre =            models.CharField(max_length=100)
    apellido =          models.CharField(max_length=100)
    tipo_sangre =       models.CharField(max_length=20)
    experiencia =       models.IntegerField()
    jornada=            models.CharField(max_length=15)
    fecha_vinculacion = models.DateField()
    cargo =             models.CharField(max_length=150)
    telefono =          models.CharField(max_length=100)
    genero =            models.CharField(max_length=15)
    fecha_nacimiento =  models.DateField()
    area    =           models.CharField(max_length=150)
    estado_empleado =   models.CharField(max_length=15) #Vinculado/Desvinculado
    jefe =              models.IntegerField()


