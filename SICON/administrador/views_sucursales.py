from django.shortcuts import render
from .forms_sucursal import SucursalForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Sucursal, Ciudad, Departamento


def listar_sucursales(request):
	sucursales = Sucursal.objects.all()
	return render(request,'lista_sucursales.html',{'sucursales':sucursales})

def crear_sucursal(request):
	sucursal = SucursalForm()
	exito = False
	#raise Exception{request}
	if request.method=='POST':
		sucursal= SucursalForm(request.POST)
	if sucursal.is_valid():
		sucursal.save()
		exito = True
		sucursal = SucursalForm()
		return HttpResponseRedirect('/sucursales/crear_sucursal')
	return render(request, 'crear_sucursal.html', {'form':sucursal,'exito':exito} )


def editar_sucursal(request, id_sucursal):
    sucursales = Sucursal.objects.all()
    sucursal = Sucursal.objects.get(pk = id_sucursal)
    form_edicion = SucursalForm(instance=sucursal, initial=sucursal.__dict__)
    if request.method == 'POST':
        form_edicion = SucursalForm(
            request.POST, instance=sucursal, initial=sucursal.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/sucursales/listar")
        else:
            return HttpResponseRedirect("/sucursales/listar")
    return render(request, 'lista_sucursales.html', {'sucursales': sucursales, 'edicion': True, 'form_edicion': form_edicion})


def eliminar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id=id)
    if sucursal.activo:
        sucursal.activo=False
    else:
        sucursal.activo=True
    sucursal.save()
    return HttpResponseRedirect("/sucursales/listar")

def cargar_ciudades(request):


	if request.method == 'POST':

		departamento_id = request.POST['departamento']
		departamento_obj = Departamento.objects.get(id = departamento_id)
		ciudades = Ciudad.objects.filter(departamento = departamento_obj)
		lista_ciudades = []
        dir_ciudad = dict()
        for ciudad in ciudades:
            dir_ciudad["id"] = str(ciudad.id)
            dir_ciudad["nombre"] = ciudad.nombre
            lista_ciudades.append(dir_ciudad)
            dir_ciudad = {}
        return JsonResponse(lista_ciudades, None, False)