from django.shortcuts import render
from .forms_orden import OrdenForm, DetalleRepuestoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Orden, DetalleRepuesto
from SICON.administrador.models import  Empleado, Repuesto, VehiculoUsado, JefeTaller
from django.contrib.auth.decorators import login_required,permission_required
import json
from django.core import serializers


@login_required(login_url='/login')
def listar_ordenes(request):
    ordenes = Orden.objects.all()
    id_sesion = request.session["id"]
    usuario = JefeTaller.objects.filter(id=id_sesion).first()
    permisos = list(usuario.get_all_permissions())
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes, 'permisos': permisos})


@login_required(login_url='/login')
def crear_orden(request):
    id_sesion = request.session["id"]
    usuario = JefeTaller.objects.filter(id=id_sesion).first()
    permisos = list(usuario.get_all_permissions())
    jefe = JefeTaller.objects.filter(id=id_sesion)
    jefe_sucursal = jefe[0]
    sucursal = jefe_sucursal.sucursal
    mecanicos = obtenerMecanicos(sucursal)
    vehiculos = obtenerVehiculos(sucursal)
    orden = OrdenForm()
    exito = False
    # raise Exception{request}
    if request.method == 'POST':
        orden = OrdenForm(request.POST)
    if orden.is_valid():
        orden.save(commit=False)
        orden.estado = False
        exito = True
        orden = OrdenForm()
        print exito
    return render(request, 'crear_orden.html', {'form': orden, 'exito': exito, 'mecanicos': mecanicos, 'permisos': permisos, 'vehiculos': vehiculos})


def devuelve_estado(request, placa_rec):
    veh_usados=VehiculoUsado.objects.filter(placa=placa_rec)
    veh_usado=None
    orden_actual=None
    if len(veh_usados)>=1:
        veh_usado=veh_usados[0]
        ordenes=Orden.objects.filter(placa=veh_usado).order_by('-fecha_inicio')
        if len(ordenes)>=1:
            orden_actual=ordenes[0]


    data = {}
    data['mensaje'] = ''
    data['estado'] = ''
    data['fecha_ini'] = ''
    data['fecha_fin'] = ''

    if orden_actual==None:
        data['mensaje'] = 'nada'
        data['estado'] = 'nada'
        data['fecha_ini'] = 'nada'
        data['fecha_fin'] = 'nada'
    else:
        data['mensaje'] = 'encontrado'
        data['estado'] = str(orden_actual.finalizado)
        data['fecha_ini'] = str(orden_actual.fecha_inicio)
        data['fecha_fin'] = str(orden_actual.fecha_fin)
    print orden_actual
    print "LLEGA A DEVUELVE ESTADO CON PLACA"
    print placa_rec

    datas = []
    datas.append(data)

    # foos = []
    # foos.append(orden_actual)
    # data = serializers.serialize('json', foos)

    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(json.dumps(datas), content_type="application/json")


def obtenerMecanicos(sucursal):
    mecanicos = Empleado.objects.filter(sucursal = sucursal, cargo = 'Mecanico')
    return mecanicos

def obtenerVehiculos(sucursal):
    vehiculos = VehiculoUsado.objects.filter(sucursal= sucursal)
    return vehiculos


@login_required(login_url='/login')
def editar_orden(request, id_sucursal):

    ordenes = Orden.objects.all()
    orden = Orden.objects.get(pk=id_sucursal)
    mecanicos = obtenerMecanicos(sucursal)
    form_edicion = OrdenForm(instance=orden, initial=orden.__dict__)

    if request.method == 'POST':
        form_edicion = OrdenForm(
            request.POST, instance=orden, initial=orden.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("listar_ordenes")
        else:
            return HttpResponseRedirect("listar_ordenes")
    return render(request, 'lista_ordenes.html',
                  {'ordenes': ordenes, 'edicion': True, 'form_edicion': form_edicion, 'mecanicos': mecanicos})

@login_required(login_url='/login')
def eliminar_orden(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()
    return HttpResponseRedirect("listar_ordenes")


# def cargar_ciudades(request):
#     if request.method == 'POST':
#         departamento_id = request.POST['departamento']
#         departamento_obj = Departamento.objects.get(id=departamento_id)
#         ciudades = Ciudad.objects.filter(departamento=departamento_obj)
#         lista_ciudades = []
#     dir_ciudad = dict()
#     for ciudad in ciudades:
#         dir_ciudad["id"] = str(ciudad.id)
#         dir_ciudad["nombre"] = ciudad.nombre
#         lista_ciudades.append(dir_ciudad)
#         dir_ciudad = {}
#     return JsonResponse(lista_ciudades, None, False)
