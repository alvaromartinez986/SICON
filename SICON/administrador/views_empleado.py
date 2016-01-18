from operator import is_
from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import JsonResponse

__author__ = 'nelson'

@login_required(login_url='/login')
def listar_empleado(request):
    id_sesion = request.session["id"]
    print "ID DEL USUARIO"
    print id
    gerente = Gerente.objects.filter(id=id_sesion)
    jefe = JefeTaller.objects.filter(id=id_sesion)
    vendedor = Vendedor.objects.filter(id=id_sesion)
    s_admin = SuperAdmin.objects.filter(id=id_sesion)
    empleados = []
    if len(gerente)>0:
        gerente=gerente[0]
        sucursal=gerente.sucursal
        print gerente.username
        print gerente
        empleados = Empleado.objects.filter(cargo='Jefe de taller', sucursal=sucursal) | Empleado.objects.filter(cargo='Vendedor', sucursal=sucursal)
    elif len(jefe)>0:
        jefe=jefe[0]
        sucursal=jefe.sucursal
        print jefe.username
        print jefe
        empleados = Empleado.objects.filter(cargo='Mecanico', sucursal=sucursal)
    elif len(vendedor)>0:
        vendedor=vendedor[0]
        sucursal=vendedor.sucursal
        print vendedor.username
        print vendedor
        empleados = []
    elif len(s_admin)>0:
        s_admin=s_admin[0]
        print s_admin.username
        print s_admin
        empleados = Empleado.objects.filter(cargo='Gerente')
    return render(request, 'lista_empleados.html', {'empleados': empleados})

@login_required(login_url='/login')
def crear_empleado(request):

    id_sesion = request.session["id"]
    gerente = Gerente.objects.filter(id=id_sesion)
    jefe = JefeTaller.objects.filter(id=id_sesion)
    vendedor = Vendedor.objects.filter(id=id_sesion)
    s_admin = SuperAdmin.objects.filter(id=id_sesion)
    empleados = []
    sucursal = None
    opciones=0
    if len(gerente)>0:
        gerente=gerente[0]
        sucursal=gerente.sucursal
        opciones=1
    elif len(jefe)>0:
        jefe=jefe[0]
        sucursal=jefe.sucursal
        opciones=2
    elif len(vendedor)>0:
        vendedor=vendedor[0]
        sucursal=vendedor.sucursal
        opciones=0
    elif len(s_admin)>0:
        s_admin=s_admin[0]
        sucursal=s_admin.sucursal
        opciones=3

    '''--------------------------------------------------------------------------------'''
    objEmpleado = Empleado(no_documento= None, emp_id=None, nombre=None, apellido=None, tipo_sangre=None, experiencia=None, jornada=None, fecha_vinculacion=None, cargo=None, telefono=None, genero=None,
                           fecha_nacimiento=None, estado_empleado=None, jefe=None, sucursal=None)
    if opciones != 3:
        objEmpleado.sucursal = sucursal
    empleado = EmpleadoForm(instance=objEmpleado, initial=objEmpleado.__dict__)
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
            user_save.groups.add(3)

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
            user_save.groups.add(4)

            user_save.save()

        elif (tipo_cargo == 'Gerente'):
            password = request.POST.get('password')
            user = GerenteForm(empleado.data)
            user_save = user.save()
            user_save.username = request.POST.get('username')
            user_save.password = make_password(password)
            user_save.first_name=request.POST.get('nombre')
            user_save.last_name=request.POST.get('apellido')
            user_save.groups.add(2)
            user_save.save()

        exito = True
    return render(request, 'crear_empleado.html', {'form': empleado, 'exito': exito, 'opciones':opciones})

def buscar_jefe(objSucursal, tipoCargo):
    idSucursal=objSucursal.id
    jefes=[]

    if (tipoCargo == 'Jefe de taller'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Gerente', estado_empleado=True)
    elif (tipoCargo == 'Vendedor'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Gerente', estado_empleado=True)
    elif (tipoCargo == 'Mecanico'):
        jefes = Empleado.objects.filter(sucursal=objSucursal, cargo='Jefe de taller', estado_empleado=True)

    jefe=None
    if len(jefes)>=1:
        jefe=jefes[0]

    return jefe

@login_required(login_url='/login')
def editar_empleado(request, id):
    id_sesion = request.session["id"]
    print "ID DEL USUARIO"
    print id
    gerente = Gerente.objects.filter(id=id_sesion)
    jefe = JefeTaller.objects.filter(id=id_sesion)
    vendedor = Vendedor.objects.filter(id=id_sesion)
    s_admin = SuperAdmin.objects.filter(id=id_sesion)
    empleados = []
    if len(gerente)>0:
        gerente=gerente[0]
        sucursal=gerente.sucursal
        print gerente.username
        print gerente
        empleados = Empleado.objects.filter(cargo='Jefe de taller', sucursal=sucursal) | Empleado.objects.filter(cargo='Vendedor', sucursal=sucursal)
    elif len(jefe)>0:
        jefe=jefe[0]
        sucursal=jefe.sucursal
        print jefe.username
        print jefe
        empleados = Empleado.objects.filter(cargo='Mecanico', sucursal=sucursal)
    elif len(vendedor)>0:
        vendedor=vendedor[0]
        print vendedor.username
        print vendedor
        empleados = []
    elif len(s_admin)>0:
        s_admin=s_admin[0]
        print s_admin.username
        print s_admin
        empleados = Empleado.objects.filter(cargo='Gerente')

    '''--------------------------------------------------------------------------------'''
    empleado = Empleado.objects.get(pk=id)
    print ("ENTRO EN EDITAR")
    usuario = User.objects.filter(pk=id)

    if len(usuario)>=1:
        usuarioeditar = User.objects.get(pk=id)
        nomusuario=usuario[0].username
        contras=""
        contras2=usuario[0].password
    else:
        usuarioeditar = None
        nomusuario=""
        contras=""
        contras2=""
    print ("username",nomusuario)
    form_edicion = EmpleadoForm(instance=empleado, initial=empleado.__dict__)
    if request.method == 'POST':
        form_edicion = EmpleadoForm(request.POST, instance=empleado, initial=empleado.__dict__)
        if form_edicion.is_valid():
            print "valido formedicion"
            #is_user = request.POST.get('check')
            cargo_emp = empleado.cargo

            if (cargo_emp=='Mecanico'):
                sucur=empleado.sucursal
                jefeHallado=buscar_jefe(sucur, cargo_emp)
                empleado.jefe=jefeHallado
                empleado.save()

            else:
                print ("ENTRO EN Else")
                username = request.POST.get('username')
                passleida = request.POST.get('password')
                password = make_password(passleida)
                usuarioeditar.username=username
                if(passleida==""):
                    print "entro a password vacio"
                    usuarioeditar.password=contras2
                else:
                    usuarioeditar.password=password
                #empleado.save()
                usuarioeditar.save()

                sucur=empleado.sucursal
                jefeHallado=buscar_jefe(sucur, cargo_emp)
                empleado.jefe=jefeHallado
                empleado.save()
                '''
                username = request.POST.get('username')
                print username
                password = request.POST.get('password')
                print password
                User.username=username
                User.password=password
                userf = UsuariosForm(request.POST, instance=usuario[0], initial=usuario[0].__dict__)
                print "pasa formedicion data"
                if userf.is_valid():
                    user_save = userf.save()
                    print "pasa user save"
                    user_save.username = username
                    user_save.password = password
                    user_save.save()
                '''
            return HttpResponseRedirect("/empleado/listar_empleados")
    return render(request, 'lista_empleados.html', {'empleados': empleados, 'edicion': True,
                                                    'form_edicion': form_edicion, 'nomusuario': nomusuario})

@login_required(login_url='/login')
def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(pk=id)
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

