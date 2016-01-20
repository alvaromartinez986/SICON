from django.db import models
from django.utils import timezone
import datetime
from administrador.models import  Empleado, Repuesto, VehiculoUsado
from django.utils.encoding import smart_unicode


class Orden(models.Model):

    numero = models.CharField(max_length=100, unique=True)
    mecanicos = models.ManyToManyField(Empleado)
    placa = models.ForeignKey(VehiculoUsado)
    observaciones = models.TextField(blank=True)
    fecha_inicio = models.DateField(default=timezone.now())
    finalizado = models.BooleanField(default=False)
    fecha_fin = models.DateField(blank=True)
    estado = models.BooleanField(default=True)


class DetalleRepuesto(models.Model):

    orden = models.ForeignKey(Orden)
    repuesto = models.ManyToManyField(Repuesto)
    cantidad = models.IntegerField()
    Estado = models.BooleanField(default=True)
