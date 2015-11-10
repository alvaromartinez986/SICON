# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Vehiculo, VehiculoNuevo, VehiculoUsado

class VehiculoNuevoForm(ModelForm):
    class Meta:
        model = VehiculoNuevo
        fields = ['cilindraje', 'linea', 'modelo', 'tipo_combustible', 'color','marca', 'valor']
        widgets = {
			'cilindraje': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Cilindraje...'}),
            'linea': forms.TextInput(attrs={'class':'form-control required','placeholder':'Línea...'}),
            'modelo': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Modelo...'}),
            'tipo_combustible' : forms.Select(attrs={'class':'form-control required'}),
            'color': forms.TextInput(attrs={'class':'form-control required','placeholder':'Color...'}),
            'marca': forms.TextInput(attrs={'class':'form-control required','placeholder':'Marca...'}),
			'valor': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Valor...'}),
	    }

class VehiculoUsadoForm(ModelForm):
    class Meta:
        model = VehiculoNuevo
        fields = ['cilindraje', 'linea', 'modelo', 'tipo_combustible', 'color','marca', 'placa', 'servicio']
        widgets = {
			'cilindraje': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Cilindraje...'}),
            'linea': forms.TextInput(attrs={'class':'form-control required','placeholder':'Línea...'}),
            'modelo': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Modelo...'}),
            'tipo_combustible' : forms.Select(attrs={'class':'form-control required'}),
            'color': forms.TextInput(attrs={'class':'form-control required','placeholder':'Color...'}),
            'marca': forms.TextInput(attrs={'class':'form-control required','placeholder':'Marca...'}),
			'placa': forms.TextInput(attrs={'class':'form-control required','placeholder':'Placa...'}),
            'servicio' : forms.Select(attrs={'class':'form-control required'}),
	    }