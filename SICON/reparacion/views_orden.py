# -*- coding: utf-8 -*-
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
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})


@login_required(login_url='/login')
def crear_orden(request):
    id_sesion = request.session["id"]
    jefe = JefeTaller.objects.filter(id=id_sesion)
    sucursal_jefe = jefe.sucursal
    Mecanicos = Empleado.objects.filter(sucursal = sucursal_jefe, cargo = 'Mecanico')
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
    return render(request, 'crear_orden.html', {'form': orden, 'exito': exito})


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
    data['placa'] = ''
    data['respuesta'] = ''

    if orden_actual==None:
        data['mensaje'] = 'nada'
        data['estado'] = 'nada'
        data['fecha_ini'] = 'nada'
        data['fecha_fin'] = 'nada'
        data['placa'] = str(placa_rec)
        data['respuesta'] = "Lo sentimos, no se encuentra ninguna orden para el vehículo" + \
                            " con placa " + str(placa_rec) + " en el sistema"
    else:
        data['mensaje'] = 'encontrado'
        data['estado'] = str(orden_actual.finalizado)
        data['fecha_ini'] = str(orden_actual.fecha_inicio)
        data['fecha_fin'] = str(orden_actual.fecha_fin)
        data['placa'] = str(placa_rec)
        if data['estado'] == 'False':
            data['respuesta'] = "El vehículo con placa " + str(placa_rec) + " todavía se encuentra" \
                                " en reparaciones, por favor consulte " \
                                "nuevamente " + "en los" + " próximos días.\n\nFecha de ingreso: " + str(orden_actual.fecha_inicio)
        else:
            data['respuesta'] = "El vehículo con placa " + str(placa_rec) + " se encuentra listo " + \
            "para ser recogido.\n\nFecha de ingreso: " + str(orden_actual.fecha_inicio) + "\n\nFecha" + \
            " de fin de reparaciones: " + str(orden_actual.fecha_fin)

    print orden_actual
    print "LLEGA A DEVUELVE ESTADO CON PLACA"
    print placa_rec

    # datas = []
    # datas.append(data)

    # foos = []
    # foos.append(orden_actual)
    # data = serializers.serialize('json', foos)

    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(json.dumps(data), content_type="application/json")


# def obtenerMecanicos(sucursal):
#     Mecanicos = Empleado.objects.filter(sucursal = sucursal_jefe, cargo = 'Mecanico')
#     lista_mecanicos = []
#     for mecanico in Mecanicos:
#         dir_mecanico["id"] = str(mecanico.id)
#         dir_mecanico["nombre"] = mecanico.nombre+" "+mecanico.apellido
#         lista_mecanicos.append(dir_mecanico)
#     return lista_mecanicos



#
# def editar_sucursal(request, id_sucursal):
#     sucursales = Sucursal.objects.all()
#     sucursal = Sucursal.objects.get(pk=id_sucursal)
#     ciudad = sucursal.ciudad
#     departamento = ciudad.departamento
#     form_edicion = SucursalForm(instance=sucursal, initial=sucursal.__dict__)
#     if request.method == 'POST':
#         form_edicion = SucursalForm(
#             request.POST, instance=sucursal, initial=sucursal.__dict__)
#         if form_edicion.has_changed():
#             if form_edicion.is_valid():
#                 form_edicion.save()
#                 return HttpResponseRedirect("/sucursales/listar")
#         else:
#             return HttpResponseRedirect("/sucursales/listar")
#     return render(request, 'lista_sucursales.html',
#                   {'sucursales': sucursales, 'edicion': True, 'form_edicion': form_edicion, 'departamento': departamento.id})
#
#
# def eliminar_sucursal(request, id):
#     sucursal = Sucursal.objects.get(id=id)
#     if sucursal.activo:
#         sucursal.activo = False
#     else:
#         sucursal.activo = True
#     sucursal.save()
#     return HttpResponseRedirect("/sucursales/listar")
#
#
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
