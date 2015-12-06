from django.forms import ModelForm
from django import forms
from .models import Sucursal, Ciudad, Departamento

__author__ = 'alvaro'




class SucursalForm(ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control chosen-select disabled="disabled" '}))
    if  True:
        ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'}))
    else:
        ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.none(), required=True, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Sucursal
        modelTwo = Departamento
        fields = [ 'nombre', 'direccion', 'telefono', 'ciudad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control required','placeholder':'Nombre...'}),
            'direccion': forms.TextInput(attrs={'class':'form-control required','placeholder':'Direccion...'}),
            'telefono' : forms.NumberInput(attrs={'class':'form-control required', 'placeholder': 'Telefono..'})
        }

