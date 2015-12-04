from django.shortcuts import render
from .forms import VehiculoNuevoForm, VehiculoUsadoForm
from django.http import HttpResponseRedirect
from .models import VehiculoNuevo,VehiculoUsado

def crear_vehiculo_nuevo(request):
    vehiculo_n = VehiculoNuevoForm()
    exito = False
    if request.method=='POST':
        vehiculo_n = VehiculoNuevoForm(request.POST)
    if vehiculo_n.is_valid():
        vehiculo_n.save()
        exito = True
        return HttpResponseRedirect('/vehiculos_nuevos/listarvn')
    return render(request, 'crear_vehiculo_nuevo.html', {'form':vehiculo_n,'exito':exito} )

def listar_vehiculos_nuevos(request):
	vehiculos_n = VehiculoNuevo.objects.all()
	return render(request,'lista_vehiculos_nuevos.html',{'vehiculos_nuevos':vehiculos_n })

def editar_vehiculo_nuevo(request, id):
	vehs_n= VehiculoNuevo.objects.all()
	veh_n = VehiculoNuevo.objects.get(id = id)
	form_edicion = VehiculoNuevoForm(instance=veh_n, initial=veh_n.__dict__)
	if request.method == 'POST':
		form_edicion = VehiculoNuevoForm(request.POST, instance=veh_n, initial=veh_n.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
		return HttpResponseRedirect("/vehiculos_nuevos/listarvn")
	return render(request, 'lista_vehiculos_nuevos.html', {'vehiculos_nuevos': vehs_n, 'edicion': True, 'form_edicion': form_edicion})

def eliminar_vehiculo_nuevo(request, id):
    veh_n = VehiculoNuevo.objects.get(id=id)
    if veh_n.activo:
        veh_n.activo=False
    else:
        veh_n.activo=True
    veh_n.save()
    return HttpResponseRedirect("/vehiculos_nuevos/listarvn")


def crear_vehiculo_usado(request):
    vehiculo_u = VehiculoUsadoForm()
    exito = False
    if request.method=='POST':
        vehiculo_u = VehiculoUsadoForm(request.POST)
    if vehiculo_u.is_valid():
        vehiculo_u.save()
        exito = True
        return HttpResponseRedirect('/vehiculos_usados/listarvu')
    return render(request, 'crear_vehiculo_usado.html', {'form':vehiculo_u,'exito':exito} )

def listar_vehiculos_usados(request):
	vehiculos_u = VehiculoUsado.objects.all()
	return render(request,'lista_vehiculos_usados.html',{'vehiculos_usados':vehiculos_u })

def editar_vehiculo_usado(request, id):
	vehs_u= VehiculoUsado.objects.all()
	veh_u = VehiculoUsado.objects.get(id = id)
	form_edicion = VehiculoUsadoForm(instance=veh_u, initial=veh_u.__dict__)
	if request.method == 'POST':
		form_edicion = VehiculoNuevoForm(request.POST, instance=veh_u, initial=veh_u.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
		return HttpResponseRedirect("/vehiculos_usados/listarvu")
	return render(request, 'lista_vehiculos_usados.html', {'vehiculos_usados': vehs_u, 'edicion': True, 'form_edicion': form_edicion})

def eliminar_vehiculo_usado(request, id):
    veh_u = VehiculoUsado.objects.get(id=id)
    if veh_u.activo:
        veh_u.activo=False
    else:
        veh_u.activo=True
    veh_u.save()
    return HttpResponseRedirect("/vehiculos_usados/listarvu")