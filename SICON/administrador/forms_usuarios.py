__author__ = 'nelson'
from django.forms import ModelForm
from django import forms
from .models import Usuarios

class UsuariosForm(ModelForm):
    class Meta:
        model=Usuarios
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control required','placeholder':'username'}),
            'password': forms.TextInput(attrs={'class':'form-control required','placeholder':'password'}),
        }
