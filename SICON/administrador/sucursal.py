from django.db import models
__author__ = 'alvaro'

class Ciudad(models.Model):

    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    latitud = models.IntegerField()
    longitud = models.IntegerField()
    departamento_id = models.IntegerField()

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=150)
    telefono = models.TextField(max_length=150)
    ciudad = models.ForeignKey(Ciudad)

