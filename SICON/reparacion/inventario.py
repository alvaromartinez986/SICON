__author__ = 'alvaro'
from django.db import models
from SICON.administrador.models import Repuesto

class Inventario (models.Model):

    repuesto = models.ForeignKey(Repuesto)
    tipo_movimiento = models.CharField(max_length = 40)
    cantidad = models.IntegerField()
    cantidad_anterior = models.IntegerField()
    cantidad_actual = models.IntegerField()
    fecha = models.DateTimeField(null=True,blank=True)



