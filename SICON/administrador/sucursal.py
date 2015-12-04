from django.db import models
from django.utils.encoding import smart_unicode

__author__ = 'alvaro'


class Departamento(models.Model):

    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    latitud = models.IntegerField()
    longitud = models.IntegerField()

    def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):

    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    latitud = models.IntegerField()
    longitud = models.IntegerField()
    departamento = models.ForeignKey(Departamento)

    def __unicode__(self):
		return self.nombre

class Sucursal(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=150)
    telefono = models.TextField(max_length=150)
    ciudad = models.ForeignKey(Ciudad)
    activo = models.BooleanField(default=True)




