from django.shortcuts import render
from .forms_empleado import EmpleadoForm
from django.http import HttpResponseRedirect
from .models import Empleado

__author__ = 'nelson'


def listar_empleado(request):
    print "hola que hace"
    empleados = Empleado.objects.all()
    print empleados


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

