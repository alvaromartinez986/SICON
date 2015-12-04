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
        return HttpResponseRedirect('/empleados/')
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito})

def editar_empleado(request, id):
	print (id)
	empleados= Empleado.objects.all()
	empleado = Empleado.objects.get(pk = id)
	form_edicion = EmpleadoForm(instance=empleado, initial=empleado.__dict__)
	if request.method == 'POST':
		form_edicion = RepuestoForm(request.POST, instance=repuesto, initial=repuesto.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
				return HttpResponseRedirect("/empleados")
		else:
			return HttpResponseRedirect("/empleados")
	return render(request, 'lista_empleados.html', {'empleados': empleados, 'edicion': True, 'form_edicion': form_edicion})
