from django.db import models

class Vehiculo(models.Model):
    cilindraje = models.IntegerField()
    linea = models.CharField(max_length=50)
    modelo = models.IntegerField()
    COMB_CHOICES = ('Gasolina', 'Gas')
    tipo_combustible = models.CharField(choices=COMB_CHOICES, max_length=50)
    color = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.linea

class VehiculoNuevo(Vehiculo):
    valor = models.IntegerField()

class VehiculoUsado(Vehiculo):
    SERVICIO_CHOICES = ('Publico', 'Privado')
    servicio = models.CharField(choices= SERVICIO_CHOICES, max_length=50)
    placa = models.CharField(max_length=6)
