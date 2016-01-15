from django.db import models
from .sucursal import Sucursal
class Marca(models.Model):

    nombre = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100)

    def __unicode__(self):
		return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca)


class Repuesto (models.Model):

	class Meta:
		permissions = (
            # Permission identifier     human-readable permission name
            ("listar_Repuestos",       "Se permite editar, activar , desactivar" ),
        )

	codigo = models.CharField(max_length = 40, unique=True)
	nombre = models.CharField(max_length = 40)
	marca  = models.CharField(max_length = 40)
	costo  = models.IntegerField(blank=True, null=True)
	marca_carro = models.ForeignKey(Marca,blank=True,null=True)
	modelo_carro = models.ForeignKey(Modelo,blank=True,null=True)
	cantidad = models.IntegerField()
	activo = models.BooleanField(default=True)
	# sucursal = models.ForeignKey(Sucursal)
