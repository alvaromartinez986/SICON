# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Empleado
from .models import Usuarios

__author__ = 'nelson'


class UsuariosForm(ModelForm):
    class Meta:
        model=Usuarios
        fields=[
            'no_documento',
            'nombre',
            'apellido',
            'tipo_sangre' ,
            'experiencia' ,
            'jornada',
            'fecha_vinculacion' ,
            'cargo' ,
            'telefono' ,
            'genero' ,
            'fecha_nacimiento',
            'area'  ,
            'estado_empleado',
            'jefe' ]
        widgets={
            'no_documento': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Numero de documento'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'tipo_sangre': forms.Select(attrs={'class':'form-control required'}),
            'experiencia' : forms.NumberInput(attrs={'class':'form-control ','placeholder':'Experiencia'}),
            'jornada': forms.Select(attrs={'class':'form-control required'}),
            'fecha_vinculacion' : forms.DateInput(attrs={'class':'form-control ','placeholder':'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control ','placeholder':'Telefono'}),
            'genero' : forms.Select(attrs={'class':'form-control required'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de nacimiento'}),
            'area'  : forms.TextInput(attrs={'class':'form-control ','placeholder':'Area'}),
            'estado_empleado': forms.Select(attrs={'class':'form-control required'}),
            'jefe': forms.TextInput(attrs={'class':'form-control ','placeholder':'Jefe'}),
        }

