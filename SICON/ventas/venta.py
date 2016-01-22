from django.db import models
from  cliente import  Cliente
from SICON.administrador.models import VehiculoNuevo

class Venta(models.Model):
    identificacion_cliente = models.ForeignKey (Cliente)
    vehiculo = models.ForeignKey (VehiculoNuevo,unique=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.identificacion