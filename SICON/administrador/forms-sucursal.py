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
            'direccion': forms.Textarea(attrs={'class':'form-control required','placeholder':'Dirección...'}),
            'telefono' : forms.Textarea(attrs={'class':'form-control required', 'placeholder': 'Telefono..'}),
            'ciudad': forms.Select(attrs={'class':'form-control required'}),
        }
