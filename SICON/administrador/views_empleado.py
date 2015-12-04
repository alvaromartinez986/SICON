from django.shortcuts import render
from .forms_empleado import EmpleadoForm
from django.http import HttpResponseRedirect
from .models import Empleado

__author__ = 'nelson'


def listar_empleado(request):
    print "hola que hace"
    empleados = Empleado.objects.all()
    return render(request,'lista_empleados.html',{'empleados':empleados})


def crear_empleado(request):
    empleado = EmpleadoForm()
    exito = False
    if request.method == 'POST':
        empleado = EmpleadoForm(request.POST)
    if empleado.is_valid():
        empleado.save()
        exito = True
        empleado = EmpleadoForm()
        return HttpResponseRedirect('/empleado/listar')
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito})

def editar_empleado(request, id):
	print (id)
	empleados= Empleado.objects.all()
	empleado = Empleado.objects.get(pk = id)
	form_edicion = EmpleadoForm(instance=empleado, initial=empleado.__dict__)
	print "holi1"
	if request.method == 'POST':
		print "holi2"
		form_edicion = EmpleadoForm(request.POST, instance=empleado, initial=empleado.__dict__)
		if form_edicion.has_changed():
			print "holi3"
			if form_edicion.is_valid():
				print "holi3"
				form_edicion.save()
				return HttpResponseRedirect("/empleado/listar")
		else:
			print "holi4"
			return HttpResponseRedirect("/empleado/listar")
	return render(request, 'lista_empleados.html', {'empleados': empleados, 'edicion': True, 'form_edicion': form_edicion})
