# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Vehiculo, VehiculoNuevo, VehiculoUsado

class VehiculoNuevoForm(ModelForm):
    class Meta:
        model = VehiculoNuevo
        fields = ['codigo', 'cilindraje','marca', 'linea', 'modelo', 'tipo_combustible', 'color','fecha_ingreso' ,'valor']
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control required','placeholder':'Código...'}),
			'cilindraje': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Cilindraje...', 'min':'0'}),
            'marca': forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Marca..'}),
            'linea': forms.TextInput(attrs={'class':'form-control required','placeholder':'Línea...'}),
            'modelo': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Modelo...', 'min':'1950'}),
            'tipo_combustible' : forms.Select(attrs={'class':'form-control required'}),
            'color': forms.TextInput(attrs={'class':'form-control required','placeholder':'Color...'}),
            'fecha_ingreso': forms.DateInput(attrs={'class':'form-control required', 'placeholder': 'Fecha de ingreso'}),
			'valor': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Valor...', 'min':'1'}),
	    }

class VehiculoUsadoForm(ModelForm):
    class Meta:
        model = VehiculoUsado
        fields = ['cilindraje', 'linea', 'modelo', 'tipo_combustible', 'color','marca', 'placa', 'servicio']
        widgets = {
            'placa': forms.TextInput(attrs={'class':'form-control required','placeholder':'Placa...'}),
			'cilindraje': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Cilindraje...'}),
            'marca': forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Marca..'}),
            'linea': forms.TextInput(attrs={'class':'form-control required','placeholder':'Línea...'}),
            'modelo': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Modelo...', 'min':'1950'}),
            'tipo_combustible' : forms.Select(attrs={'class':'form-control required'}),
            'color': forms.TextInput(attrs={'class':'form-control required','placeholder':'Color...'}),
            'servicio' : forms.Select(attrs={'class':'form-control required'}),
	    }