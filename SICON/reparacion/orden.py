from django.db import models
from django.utils import timezone
import datetime
from SICON.administrador.models import  Empleado, Repuesto, VehiculoUsado, Sucursal
from django.utils.encoding import smart_unicode


class Orden(models.Model):


    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_ordenes",       "Se permite editar, activar , desactivar, listar" ),
        )

    numero = models.CharField(max_length=100, unique=True)
    mecanicos = models.ManyToManyField(Empleado)
    placa = models.ForeignKey(VehiculoUsado)
    observaciones = models.TextField(blank=True)
    fecha_inicio = models.DateField(default=timezone.now())
    finalizado = models.BooleanField()
    fecha_fin = models.DateField(blank=True,null=True)
    sucursal = models.ForeignKey(Sucursal)


class DetalleRepuesto(models.Model):



    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_ordenes_repuestos",       "Se permite editar, activar , desactivar, listar" ),
        )

    orden = models.ForeignKey(Orden)
    repuesto = models.ManyToManyField(Repuesto)
    cantidad = models.IntegerField()

