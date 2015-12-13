from django.forms import ModelForm
from django import forms
from .models import Orden, DetalleRepuesto

__author__ = 'alvaro'




class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = [ 'numero', 'placa', 'mecanicos', 'fecha_inicio', 'finalizada', 'fecha_fin', 'observaciones']
        widgets = {
            'numero': forms.TextInput(attrs={'class':'form-control required','placeholder':'Numero de la orden...'}),
            'placa': forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Placa del vehiculo..'}),
            'mecanicos' : forms.SelectMultiple(attrs={'class':'chosen-select required', 'placeholder': 'Mecanicos para la orden..'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'chosen-select required', 'placeholder': 'Fecha de inicio..'}),
            'finalizado': forms.BooleanField(attrs={'class':'chosen-select required', 'placeholder': 'Termino el trabajo..'}),
            'fecha_fin': forms.DateInput(attrs={'class':'chosen-select required', 'placeholder': 'Fecha de fin..'}),
            'observaciones' : forms.TextInput(attrs={'class':'form-control required', 'placeholder': 'Observaciones de la orden..'}),
        }

class DetalleRepuestoForm(ModelForm):
    class Meta:
        model = DetalleRepuesto
        fields = ['orden', 'repuesto', 'cantidad']
        widgets = {
            'orden': forms.Select(attrs={'class':'form-control required','placeholder':'Numero de la orden...'}),
            'repuesto': forms.Select(attrs={'class':'form-control required','placeholder':'Repuesto...'}),
            'cantidad': forms.IntegerField(attrs= {'class':'form-control required','placeholder':'Numero de repuestos utilizados..'}),
        }