from django.db import models
from .sucursal import Sucursal, Ciudad

# Create your models here.
class Repuesto (models.Model):

	codigo = models.CharField(max_length = 40, unique=True)
	nombre = models.CharField(max_length = 40, unique=True)
	marca  = models.CharField(max_length = 40)
	costo  = models.IntegerField(blank=True, null=True)
	marca_carro = models.CharField(max_length = 40)
	modelo_carro = models.CharField(max_length = 40)
	cantidad = models.IntegerField()
	
	
	
	
	
	
