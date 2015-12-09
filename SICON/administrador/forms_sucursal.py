from django.forms import ModelForm
from django import forms
from .models import Sucursal, Ciudad, Departamento

__author__ = 'alvaro'




class SucursalForm(ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control disabled="disabled" '}))

    class Meta:
        model = Sucursal
        modelTwo = Departamento
        fields = [ 'nombre', 'direccion', 'telefono', 'ciudad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control required','placeholder':'Direccion...'}),
            'telefono' : forms.NumberInput(attrs={'class':'form-control required', 'placeholder': 'Telefono..', 'min':'1'}),
            'ciudad' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Ciudad..'}),
        }

