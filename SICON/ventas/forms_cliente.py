# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion', 'nombres','apellidos', 'telefono']
        widgets = {
            'identificacion': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Identificación...', 'min':'0'}),
			'nombres': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombres...'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control required','placeholder':'Apellidos...'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control required','placeholder':'Teléfono...', 'min':'0'})
	    }