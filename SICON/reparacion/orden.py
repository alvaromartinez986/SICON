from django.db import models
from datetime import date
from administrador.models import  Empleado, Repuestos, VehiculoUsado
from django.utils.encoding import smart_unicode


class Orden(models.Model):

    numero = models.CharField(max_length=100, unique=True)
    mecanicos = models.ManyToManyField(Empleado)
    placa = models.ForeignKey(VehiculoUsado)
    observaciones = models.TextField()
    fecha_inicio = models.DateField(default=datetime.now)
    finalizada = models.BooleanField(default=False)
    fecha_fin = models.DateField(blank=True)
    estado = models.BooleanField(default=True)


class DetalleRepuesto(models.Model):

    orden = models.ForeignKey()
    repuesto = models.ManyToManyField(Repuestos)
    cantidad = models.IntegerField()
    Estado = models.BooleanField(default=True)
