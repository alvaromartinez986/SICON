from django.forms import ModelForm
from django import forms
from .models import Empleado

__author__ = 'nelson'


class EmpleadoForm(ModelForm):
    class Meta:
        model=Empleado
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
            'no_documento': forms.NumberInput(attrs={'class':'form-control required','placeholder':'no_documento'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control','placeholder':'apellido'}),
            'tipo_sangre': forms.TextInput(attrs={'class':'form-control ','placeholder':'tipo_sangre'}),
            'experiencia' : forms.NumberInput(attrs={'class':'form-control ','placeholder':'experiencia'}),
            'jornada': forms.TextInput(attrs={'class':'form-control ','placeholder':'jornada'}),
            'fecha_vinculacion' : forms.DateInput(attrs={'class':'form-control ','placeholder':'fecha_vinculacion'}),
            'cargo': forms.TextInput(attrs={'class':'form-control ','placeholder':'cargo'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control ','placeholder':'telefono'}),
            'genero' : forms.TextInput(attrs={'class':'form-control ','placeholder':'genero'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control ','placeholder':'fecha_nacimiento'}),
            'area'  : forms.TextInput(attrs={'class':'form-control ','placeholder':'area'}),
            'estado_empleado': forms.TextInput(attrs={'class':'form-control ','placeholder':'estado_empleado'}),
            'jefe': forms.TextInput(attrs={'class':'form-control ','placeholder':'jefe'}),
        }

