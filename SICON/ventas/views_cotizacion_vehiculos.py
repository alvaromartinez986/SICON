from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrador.models import VehiculoNuevo

def cotizar_vehiculos(request):
    vehiculos_n = VehiculoNuevo.objects.all()
    return render(request,'cotizacion_vehiculos.html',{'vehiculos_nuevos':vehiculos_n })
