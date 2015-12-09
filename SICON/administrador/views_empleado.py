from operator import is_
from django.shortcuts import render
from .forms_empleado import EmpleadoForm
from .forms_usuarios import UsuariosForm
from django.http import HttpResponseRedirect
from .models import Empleado
from .models import Usuarios

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
        is_user = request.POST.get('check')
        if (is_user ==None):
            empleado.save()

        else:
			  username = request.POST.get('username')
			  password = request.POST.get('password')
			  user = UsuariosForm(empleado.data)
			  user_save =user.save()
			  user_save.username=username
			  user_save.password=password
			  user_save.save()


        
        exito = True

        # empleado = EmpleadoForm()

        #return HttpResponseRedirect('/empleado/listar')
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito})

def editar_empleado(request, id):
	print (id)
	empleados= Empleado.objects.all()
	empleado = Empleado.objects.get(pk = id)
	form_edicion = EmpleadoForm(instance=empleado, initial=empleado.__dict__)
	if request.method == 'POST':
		form_edicion = EmpleadoForm(request.POST, instance=empleado, initial=empleado.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
				return HttpResponseRedirect("/empleado/listar")
		else:
			print "holi4"
			return HttpResponseRedirect("/empleado/listar")
	return render(request, 'lista_empleados.html', {'empleados': empleados, 'edicion': True, 'form_edicion': form_edicion})
