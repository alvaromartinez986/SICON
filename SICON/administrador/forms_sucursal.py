from django.forms import ModelForm
from django import forms
from .models import Sucursal, Ciudad

__author__ = 'alvaro'




class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = [ 'nombre', 'direccion', 'telefono', 'ciudad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control required','placeholder':'Direccion...'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control required', 'placeholder': 'Telefono..'}),
            'ciudad': forms.Select(attrs={'class':'form-control required'}),
        }
