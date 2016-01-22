from django.shortcuts import render
from .forms import RepuestoForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import Repuesto,Marca,Modelo,Empleado,Gerente
import json
# Create your views here.
def crear_repuesto(request):
	repuesto = RepuestoForm()
	exito = False
	if request.method=='POST':
		repuesto = RepuestoForm(request.POST)
		id = request.session["id"]
		id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
		empleado = Empleado.objects.filter (emp_id = id_empleado).first()
	if repuesto.is_valid():
		repuest =  repuesto.save(commit=False)
		repuest.sucursal = empleado.sucursal
		repuest.save()
		exito = True
		repuesto = RepuestoForm()
		return HttpResponseRedirect('/repuestos/')
	return render(request, 'crear_repuesto.html', {'form':repuesto,'exito':exito} )

def listar_repuestos(request):
	id = request.session["id"]
	print id
	id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
	empleado = Empleado.objects.filter (emp_id = id_empleado).first()
	repuestos = Repuesto.objects.filter(sucursal = empleado.sucursal)
	return render(request,'lista_repuestos.html',{'repuestos':repuestos})

def editar_repuesto(request, id):
	id_session = request.session["id"]
	id_empleado = Gerente.objects.filter (user_ptr_id = id_session).first().empleado_ptr_id
	empleado = Empleado.objects.filter (emp_id = id_empleado).first()
	repuestos = Repuesto.objects.filter(sucursal = empleado.sucursal)
	repuesto = Repuesto.objects.get(pk = id)
	print "marca"
	print repuesto.marca_carro
	modelos = Modelo.objects.filter (marca = repuesto.marca_carro)
	print "Modelos"
	print modelos
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
