# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Repuesto
from .models import Gerente,Empleado
from django.http import request
from django.contrib.sessions.backends.db import SessionStore


class RepuestoForm(ModelForm):
    class Meta:
        model = Repuesto
        fields = ['codigo','nombre', 'marca', 'costo','marca_carro','modelo_carro','cantidad']
        widgets = {
        'codigo': forms.TextInput(attrs={'class':'form-control required','placeholder':'Código'}),
        'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
        'marca': forms.TextInput(attrs={'class':'form-control','placeholder':'Marca'}),
        'costo': forms.NumberInput(attrs={'class':'form-control','placeholder':'Costo'}),
        'marca_carro': forms.Select(attrs={'class':'chosen-select required','placeholder':'Marca del carro'}),
        'modelo_carro': forms.TextInput(attrs={'class':'form-control','placeholder':'Linea del carro'}),
        'cantidad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad inicial'}),
    }


    #
    # def clean_codigo(self):
    #     s = SessionStore()
    #     codigo = self.cleaned_data.get('codigo', '')
    #     id= request.data
    #     print "id"
    #     print id
    #     id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
    #     empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    #     repuesto = Repuesto.objects.filter(codigo = codigo, sucursal = empleado.sucursal)
    #
    #     if repuesto is not None:
    #         raise forms.ValidationError("el codigo ya existe en la base de datos")
    #
    #     return codigo

