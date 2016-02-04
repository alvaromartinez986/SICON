from django.db import models
from  cliente import  Cliente
from SICON.administrador.models import VehiculoNuevo,Empleado

class Venta(models.Model):
    identificacion_cliente = models.ForeignKey (Cliente)
    identificacion_vendedor = models.ForeignKey (Empleado)
    total = models.FloatField(null=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.identificacion




class DetalleVenta (models.Model):
    id_venta = models.ForeignKey (Venta)
    vehiculo = models.OneToOneField (VehiculoNuevo)
    costo = models.IntegerField(null=True)
    dcto = models.FloatField(null=True)
    costo_venta = models.FloatField(null=True)


