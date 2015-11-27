from django.shortcuts import render
from .forms_sucursal import SucursalForm
from django.http import HttpResponseRedirect
from .models import Sucursal


def listar_sucursales(request):
	sucursales = Sucursal.objects.all()
	return render(request,'lista_sucursales.html',{'sucursales':sucursales})

def crear_sucursal(request):
	sucursal = SucursalForm()
	exito = False
	if request.method=='POST':
		repuesto = SucursalForm(request.POST)
	if sucursal.is_valid():
		sucursal.save()
		exito = True
		repuesto = SucursalForm()
		return HttpResponseRedirect('/sucursales/')
	return render(request, 'crear_sucursal.html', {'form':sucursal,'exito':exito} )