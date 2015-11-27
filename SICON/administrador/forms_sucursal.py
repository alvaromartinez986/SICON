from django.forms import ModelForm
from django import forms
from .models import Sucursal, Ciudad, Departamento

__author__ = 'alvaro'




class SucursalForm(ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.none(), required=True, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Sucursal
        modelTwo = Departamento
        fields = [ 'nombre', 'direccion', 'telefono', 'ciudad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control required','placeholder':'Direccion...'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control required', 'placeholder': 'Telefono..'})
        }

