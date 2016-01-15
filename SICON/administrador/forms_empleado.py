# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Empleado
from .models import JefeTaller
from .models import Gerente
from .models import Vendedor
from .models import SuperAdmin
from .models import Sucursal
from django.forms.fields import DateField

__author__ = 'nelson'


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'no_documento',
            'nombre',
            'apellido',
            'tipo_sangre',
            'experiencia',
            'jornada',
            'fecha_vinculacion',
            'cargo',
            'telefono',
            'genero',
            'fecha_nacimiento',
            'sucursal']
        widgets = {
            'no_documento': forms.NumberInput(
                attrs={'class': 'form-control required', 'placeholder': 'Numero de documento', 'min': '1'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control required'}),
            'experiencia': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Experiencia', 'min': '0'}),
            'jornada': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_vinculacion': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required','onclick':'myFunction()'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefono'}),
            'genero': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de nacimiento'}),
            'sucursal' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Sucursal..'}),
        }


class JefeTallerForm(ModelForm):
    class Meta:
        model = JefeTaller
        fields = [
            'no_documento',
            'nombre',
            'apellido',
            'email',
            'tipo_sangre',
            'experiencia',
            'jornada',
            'fecha_vinculacion',
            'cargo',
            'telefono',
            'genero',
            'fecha_nacimiento',
            'sucursal']
        widgets = {
            'no_documento': forms.NumberInput(
                attrs={'class': 'form-control required', 'placeholder': 'Numero de documento', 'min': '1'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control required'}),
            'experiencia': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Experiencia', 'min': '0'}),
            'jornada': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_vinculacion': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required','onclick':'myFunction()'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefono'}),
            'genero': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de nacimiento'}),
            'sucursal' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Sucursal..'}),
        }

class GerenteForm(ModelForm):
    class Meta:
        model = Gerente
        fields = [
            'no_documento',
            'nombre',
            'apellido',
            'email',
            'tipo_sangre',
            'experiencia',
            'jornada',
            'fecha_vinculacion',
            'cargo',
            'telefono',
            'genero',
            'fecha_nacimiento',
            'sucursal']
        widgets = {
            'no_documento': forms.NumberInput(
                attrs={'class': 'form-control required', 'placeholder': 'Numero de documento', 'min': '1'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control required'}),
            'experiencia': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Experiencia', 'min': '0'}),
            'jornada': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_vinculacion': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required','onclick':'myFunction()'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefono'}),
            'genero': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de nacimiento'}),
            'sucursal' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Sucursal..'}),
        }

class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            'no_documento',
            'nombre',
            'apellido',
            'email',
            'tipo_sangre',
            'experiencia',
            'jornada',
            'fecha_vinculacion',
            'cargo',
            'telefono',
            'genero',
            'fecha_nacimiento',
            'sucursal']
        widgets = {
            'no_documento': forms.NumberInput(
                attrs={'class': 'form-control required', 'placeholder': 'Numero de documento', 'min': '1'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control required'}),
            'experiencia': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Experiencia', 'min': '0'}),
            'jornada': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_vinculacion': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required','onclick':'myFunction()'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefono'}),
            'genero': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de nacimiento'}),
            'sucursal' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Sucursal..'}),
        }

class SuperAdminForm(ModelForm):
    class Meta:
        model = SuperAdmin
        fields = [
            'no_documento',
            'nombre',
            'apellido',
            'email',
            'tipo_sangre',
            'experiencia',
            'jornada',
            'fecha_vinculacion',
            'cargo',
            'telefono',
            'genero',
            'fecha_nacimiento',
            'sucursal']
        widgets = {
            'no_documento': forms.NumberInput(
                attrs={'class': 'form-control required', 'placeholder': 'Numero de documento', 'min': '1'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email' : forms.TextInput(attrs={'type':'email','class':'form-control required','placeholder':'Correo Electronico...'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control required'}),
            'experiencia': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Experiencia', 'min': '0'}),
            'jornada': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_vinculacion': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de vinculacion'}),
            'cargo': forms.Select(attrs={'class':'form-control required','onclick':'myFunction()'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefono'}),
            'genero': forms.Select(attrs={'class': 'form-control required'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control required', 'placeholder': 'Fecha de nacimiento'}),
            'sucursal' : forms.Select(attrs={'class':'chosen-select required', 'placeholder': 'Sucursal..'}),
        }