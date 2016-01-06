from operator import is_
from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from .forms_usuarios import UsuariosForm
from django.http import HttpResponseRedirect
from .models import Empleado
from .models import Usuarios
from django.contrib.auth.hashers import make_password,is_password_usable
from .models import Sucursal
from django.http import JsonResponse

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
        tipo_cargo = request.POST.get('cargo')
        print tipo_cargo
        print empleado.is_valid()
    if empleado.is_valid():
        is_user = request.POST.get('check')

        if (tipo_cargo == 'Mecanico'):
            user_save = empleado.save()

            sucur=user_save.sucursal
            jefeHallado=buscar_jefe(sucur, tipo_cargo)
            user_save.jefe=jefeHallado

            user_save.save()

        elif (tipo_cargo == 'Jefe de taller'):
            password = request.POST.get('password')
            user = JefeTallerForm(empleado.data)
            user_save = user.save()
            user_save.username = request.POST.get('username')
            user_save.password = make_password(password)
            user_save.first_name=request.POST.get('nombre')
            user_save.last_name=request.POST.get('apellido')

            sucur=user_save.sucursal
            jefeHallado=buscar_jefe(sucur, tipo_cargo)
            user_save.jefe=jefeHallado

            user_save.save()

        elif (tipo_cargo == 'Vendedor'):
            password = request.POST.get('password')
            user = VendedorForm(empleado.data)
            user_save = user.save()
            user_save.username = request.POST.get('username')
            user_save.password = make_password(password)
            user_save.first_name=request.POST.get('nombre')
            user_save.last_name=request.POST.get('apellido')

            sucur=user_save.sucursal
            jefeHallado=buscar_jefe(sucur, tipo_cargo)
            user_save.jefe=jefeHallado

            user_save.save()

        elif (tipo_cargo == 'Gerente'):
            password = request.POST.get('password')
            user = GerenteForm(empleado.data)
            user_save = user.save()
            user_save.username = request.POST.get('username')
            user_save.password = make_password(password)
            user_save.first_name=request.POST.get('nombre')
            user_save.last_name=request.POST.get('apellido')
            user_save.save()

        exito = True
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito})

def buscar_jefe(objSucursal, tipoCargo):
    idSucursal=objSucursal.id
    jefes=[]

    if (tipoCargo == 'Jefe de taller'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Gerente')
    elif (tipoCargo == 'Vendedor'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Gerente')
    elif (tipoCargo == 'Mecanico'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Jefe de taller')

    jefe=None
    if len(jefes)>=1:
        jefe=jefes[0]

    return jefe

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

def cargar_sucursales(request):
    if request.method == 'POST':
        sucursales = Sucursal.objects.all()
        lista_sucursales = []
    dir_sucursal = dict()
    for sucursal in sucursales:
        dir_sucursal["id"] = str(sucursal.id)
        dir_sucursal["nombre"] = sucursal.nombre
        lista_sucursales.append(dir_sucursal)
        dir_sucursal = {}
    return JsonResponse(lista_sucursales, None, False)

