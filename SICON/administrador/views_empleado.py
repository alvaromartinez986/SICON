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
    return render(request, 'lista_empleados.html', {'empleados': empleados})


def crear_empleado(request):
    empleado = EmpleadoForm()
    exito = False

    if request.method == 'POST':
        empleado = EmpleadoForm(request.POST)
    if empleado.is_valid():
        is_user = request.POST.get('check')
        if (is_user == None):
            empleado.save()

        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = UsuariosForm(empleado.data)
            user_save = user.save()
            user_save.username = username
            user_save.password = password
            user_save.save()

        exito = True

        # empleado = EmpleadoForm()

        # return HttpResponseRedirect('/empleado/listar')
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito})


def editar_empleado(request, id):
    empleados = Empleado.objects.all()
    empleado = Empleado.objects.get(pk=id)

    usuario = Usuarios.objects.filter(pk=id)
    if len(usuario)>=1:
        nomusuario=usuario[0].username
        contras=usuario[0].password
    else:
        nomusuario=""
        contras=""

    form_edicion = EmpleadoForm(instance=empleado, initial=empleado.__dict__)
    if request.method == 'POST':
        form_edicion = EmpleadoForm(request.POST, instance=empleado, initial=empleado.__dict__)
        if form_edicion.is_valid():
            print "valido formedicion"
            is_user = request.POST.get('check')
            if (is_user == None):
                empleado.save()
            else:
                username = request.POST.get('username')
                print username
                password = request.POST.get('password')
                print password
                userf = UsuariosForm(request.POST, instance=usuario[0], initial=usuario[0].__dict__)
                print "pasa formedicion data"
                if userf.is_valid():
                    user_save = userf.save()
                    print "pasa user save"
                    user_save.username = username
                    user_save.password = password
                    user_save.save()
            return HttpResponseRedirect("/empleado/listar_empleados")
    return render(request, 'lista_empleados.html', {'empleados': empleados, 'edicion': True,
                                                    'form_edicion': form_edicion, 'nomusuario': nomusuario,
                                                    'contras': contras})


def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if empleado.estado_empleado:
        empleado.estado_empleado = False
    else:
        empleado.estado_empleado = True
    empleado.save()
    return HttpResponseRedirect("/empleado/listar_empleados")
