# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode

__author__ = 'nelson'

class Empleado(models.Model):
    no_documento =      models.IntegerField(unique=True)
    nombre =            models.CharField(max_length=100)
    apellido =          models.CharField(max_length=100)
    
    OMAS= 'O+'
    OMENOS= 'O-'
    AMAS= 'A+'
    AMENOS= 'A-'
    BMAS= 'B+'
    BMENOS= 'B-'
    ABMAS= 'AB+'
    ABMENOS= 'AB-'
    TIPO_CHOICES = ((OMAS, 'O+'), (OMENOS, 'O-'), (AMAS, 'A+'), (AMENOS, 'A-'), 
    (BMAS, 'B+'), (BMENOS, 'B-'), (ABMAS, 'AB+'), (ABMENOS, 'AB-'))
    tipo_sangre =       models.CharField(choices=TIPO_CHOICES, max_length=20)
    
    experiencia =       models.IntegerField()
    
    MANANA= 'Mañana'
    TARDE= 'Tarde'
    NOCHE= 'Noche'
    JORNADA_CHOICES = ((MANANA, 'Mañana'), (TARDE, 'Tarde'), (NOCHE, 'Noche'))
    jornada=            models.CharField(choices=JORNADA_CHOICES, max_length=15)
    
    fecha_vinculacion = models.DateField(blank=True)
    
    VEND='Vendedor'
    JT='Jefe de taller'
    GER='Gerente'
    MEC='Mecánico' 
    CARGO_CHOICES = ((VEND, 'Vendedor'), (JT, 'Jefe de taller'), (GER, 'Gerente'), (MEC,'Mecánico')) 
    cargo =             models.CharField(choices= CARGO_CHOICES, max_length=150)
    telefono =          models.CharField(max_length=150)
    
    MASC= 'Masculino'
    FEM= 'Femenino'
    GEN_CHOICES = ((MASC, 'Masculino'), (FEM, 'Femenino'))
    genero =            models.CharField(choices=GEN_CHOICES, max_length=15)
    
    fecha_nacimiento =  models.DateField()
    area    =           models.CharField(max_length=150)
    
    VINC='Vinculado'
    DESV='Desvinculado'
    VINC_CHOICES = ((VINC,'Vinculados'), (DESV,'Desvinculado'))
    estado_empleado =   models.CharField(choices=VINC_CHOICES, max_length=15) #Vinculado/Desvinculado
    jefe =              models.IntegerField()
