from django.db import models

class Vehiculo(models.Model):
    cilindraje = models.IntegerField()
    marca = models.CharField(max_length=50)
    linea = models.CharField(max_length=50)
    modelo = models.IntegerField()
    #TIPOS DE COMBUSTIBLE
    GASOLINA='Gasolina'
    GAS= 'Gas'
    COMB_CHOICES = ((GASOLINA, 'Gasolina'), (GAS, 'Gas'))
    tipo_combustible = models.CharField(choices=COMB_CHOICES, max_length=50)
    color = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.linea

class VehiculoNuevo(Vehiculo):
    valor = models.IntegerField()
    codigo = models.CharField(max_length=10,unique=True, default=01)

class VehiculoUsado(Vehiculo):
    #TIPOS DE SERVICIO
    PUBLICO= 'Publico'
    PRIVADO= 'Prviado'
    SERVICIO_CHOICES = ((PUBLICO,'Publico'), (PRIVADO,'Privado'))
    servicio = models.CharField(choices= SERVICIO_CHOICES, max_length=50)
    placa = models.CharField(max_length=6,unique=True)
