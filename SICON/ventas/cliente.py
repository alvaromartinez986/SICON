from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField()
    def __str__(self):
        return self.identificacion