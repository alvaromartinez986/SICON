# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Repuesto
class RepuestoForm(ModelForm):
	
	class Meta:
		
		model = Repuesto
		fields = ['codigo','nombre', 'marca', 'costo','marca_carro','modelo_carro','cantidad']
		widgets = {
		'codigo': forms.TextInput(attrs={'class':'form-control required','placeholder':'Código'}),
		'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		'marca': forms.TextInput(attrs={'class':'form-control','placeholder':'Marca'}),
		'costo': forms.NumberInput(attrs={'class':'form-control','placeholder':'Costo'}),
		'marca_carro': forms.Select(attrs={'class':'form-control','placeholder':'Marca del carro'}),
		'modelo_carro': forms.Select(attrs={'class':'form-control','placeholder':'Linea del carro'}),
		'cantidad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad inicial'}),
	}
