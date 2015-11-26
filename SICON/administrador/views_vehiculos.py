from django.shortcuts import render
from .forms import VehiculoNuevoForm, VehiculoNuevoForm
from django.http import HttpResponseRedirect
from .models import VehiculoNuevo,VehiculoUsado

def crear_vehiculo_nuevo(request):
    vehiculo_n = (VehiculoNuevo)
    exito = False
    if request.method=='POST':
        vehiculo_n = VehiculoNuevoForm(request.POST)
    if vehiculo_n.is_valid():
        vehiculo_n.save()
        exito = True
        vehiculo_n= VehiculoNuevoForm()
        return HttpResponseRedirect('/vehiculos_nuevos/')
    return render(request, 'crear_vehiculo_nuevo.html', {'form':vehiculo_n,'exito':exito} )

def listar_vehiculos_nuevos(request):
	vehiculos_n = VehiculoNuevo.objects.all()
	return render(request,'lista_vehiculos_nuevos.html',{'vehiculos_nuevos':vehiculos_n })