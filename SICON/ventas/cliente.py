from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(unique=True, max_length=30)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.identificacion