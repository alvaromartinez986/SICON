from django.shortcuts import render
from .forms import RepuestoForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import Repuesto,Marca,Modelo
import json
# Create your views here.
def crear_repuesto(request):
	repuesto = RepuestoForm()
	exito = False
	if request.method=='POST':
		repuesto = RepuestoForm(request.POST)
	if repuesto.is_valid():
		repuesto.save()
		exito = True
		repuesto = RepuestoForm()
		return HttpResponseRedirect('/repuestos/')
	return render(request, 'crear_repuesto.html', {'form':repuesto,'exito':exito} )

def listar_repuestos(request):
	repuestos = Repuesto.objects.all()
	return render(request,'lista_repuestos.html',{'repuestos':repuestos})

def editar_repuesto(request, id):
	repuestos= Repuesto.objects.all()
	repuesto = Repuesto.objects.get(pk = id)
	print "marca"
	print repuesto.marca_carro
	modelos = Modelo.objects.filter (marca = repuesto.marca_carro)
	form_edicion = RepuestoForm(instance=repuesto, initial=repuesto.__dict__)
	if request.method == 'POST':
		form_edicion = RepuestoForm(request.POST, instance=repuesto, initial=repuesto.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
				return HttpResponseRedirect("/repuestos")
		else:
			return HttpResponseRedirect("/repuestos")
	return render(request, 'lista_repuestos.html', {'modelos': modelos,'repuestos': repuestos,'repuesto':repuesto, 'edicion': True, 'form_edicion': form_edicion})

def inventario (request,id):
	print ("inventario")
	repuestos= Repuesto.objects.all()
	repuesto = Repuesto.objects.get(pk = id)
	if request.method == 'POST':
		cantidad = request.POST['cantidad_inv']
		repuesto.cantidad+= int (cantidad)
		repuesto.save()
		return HttpResponseRedirect('/repuestos/')
	return render(request, 'lista_repuestos.html', {'repuestos': repuestos, 'inventario': True, 'rep': repuesto})


def cargar_modelos (request):
		opcion =request.GET['option']
		modelos = Modelo.objects.filter(marca = opcion)
		string_respuesta = ""
		for modelo in modelos:
			string_respuesta += str(modelo.id)+":"+modelo.nombre+","
		string_respuesta = string_respuesta[0:-1]

		return HttpResponse(string_respuesta)


def eliminar_repuesto(request, id):
	repuesto= Repuesto.objects.get(id=id)
	if repuesto.activo:
		repuesto.activo = False
	else:
		repuesto.activo = True
	repuesto.save()
	return HttpResponseRedirect("/repuestos")
