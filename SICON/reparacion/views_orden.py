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
from django.utils import timezone
import datetime


@login_required(login_url='/login')
def listar_ordenes(request):
    id_sesion = request.session["id"]
    usuario = JefeTaller.objects.filter(id=id_sesion).first()
    sucursal = usuario.sucursal
    permisos = list(usuario.get_all_permissions())
    ordenes = Orden.objects.filter(sucursal = sucursal)
    print(sucursal)
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes, 'permisos': permisos, 'edicion': False})


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
        ordenModelo = orden.save(commit=False)
        ordenModelo.sucursal = sucursal
        ordenModelo.finalizado = False
        exito = True
        ordenModelo.save()
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


def obtenerMecanicos(sucursal):
    mecanicos = Empleado.objects.filter(sucursal = sucursal, cargo = 'Mecanico')
    return mecanicos

def obtenerVehiculos(sucursal):
    vehiculos = VehiculoUsado.objects.filter(sucursal= sucursal)
    return vehiculos


@login_required(login_url='/login')
def editar_orden(request, id_orden):
    ordenes = Orden.objects.all()
    id_sesion = request.session["id"]
    orden = Orden.objects.get(pk=id_orden)
    jefe = JefeTaller.objects.filter(id=id_sesion)
    jefe_sucursal = jefe[0]
    permisos = list(jefe_sucursal.get_all_permissions())
    sucursal = jefe_sucursal.sucursal
    ordenes = Orden.objects.filter(sucursal = sucursal)
    vehiculos = obtenerVehiculos(sucursal)
    mecanicos = obtenerMecanicos(sucursal)
    form_edicion = OrdenForm(instance=orden, initial=orden.__dict__)

    if request.method == 'POST':
        print (request.POST)
        form_edicion = OrdenForm(
            request.POST, instance=orden, initial=orden.__dict__)


        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                print(form_edicion)
                return HttpResponseRedirect("/reparacion/listar_ordenes")
        else:
            return HttpResponseRedirect("/reparacion/listar_ordenes")
    return render(request, 'lista_ordenes.html',
                  {'ordenes': ordenes, 'edicion': True, 'form_edicion': form_edicion, 'mecanicos': mecanicos, 'vehiculos':vehiculos, 'permisos': permisos})

@login_required(login_url='/login')
def eliminar_orden(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()
    return HttpResponseRedirect("/reparacion/listar_ordenes")

@login_required(login_url='/login')
def finalizar_orden(request, id):

    orden = Orden.objects.get(id=id)
    print (orden.fecha_fin)
    if orden.finalizado:
        orden.finalizado = False
        orden.fecha_fin = None
    else:
        orden.finalizado = True
        orden.fecha_fin = timezone.now()
    orden.save()
    return HttpResponseRedirect("/reparacion/listar_ordenes")


@login_required(login_url='/login')
def editar_detalle_repuesto(request, id_orden):

    ordenes = Orden.objects.all()
    ordenRep = Orden.objects.get(pk=id_orden)
    detalles = DetalleRepuesto.objects.all()
    id_sesion = request.session["id"]
    jefe = JefeTaller.objects.filter(id=id_sesion)
    jefe_sucursal = jefe[0]
    permisos = list(jefe_sucursal.get_all_permissions())
    sucursal = jefe_sucursal.sucursal
    ordenes = Orden.objects.filter(sucursal = sucursal)
    repuestos = Repuesto.objects.filter(sucursal = sucursal)
    opcion_repuestos = True
    # form_detalle = DetalleRepuestoForm()
    # form_detalles = []
    # for detalle in detalles:
    #
    #     form_detalle = DetalleRepuestoForm(instance=detalle, initial=orden.__dict__)
    #     form_detalles.append(form_detalle)
    #
    #
    if request.method == 'POST':
        tamano = (len(request.POST)-1)/2
        for i in  range(tamano+1):
            i=+1;
            num = 200+i

            detalleForm = DetalleRepuestoForm()
            detalle = detalleForm.save(commit=False)
            detalle.cantidad = request.POST['detalle'+str(num)+'cantidad']
            detalle.orden = ordenRep


            detalle.save();
            detalle.repuesto.add(request.POST['detalle'+str(num)+'repuesto'])
            detalle.save()
        opcion_repuestos = False
    detalles = DetalleRepuesto.objects.filter(orden = id_orden)
    return render(request, 'lista_ordenes.html',
                  {'repuestos': repuestos, 'opcion_repuestos': True, 'permisos': permisos,
                   'ordenes':ordenes, 'detalles': detalles, 'ordenRep':ordenRep})

# def crear_detalle_repuesto(request, id_orden):
#
#
#
# #     print(request.POST)
# #
# #     ordenes = Orden.objects.all()
# #     detalles = DetalleRepuesto.objects.all()
# #     ordenRep = Orden.objects.get(pk=id_orden)
# #
# #     id_sesion = request.session["id"]
# #     detalles = DetalleRepuesto.objects.filter(orden = id_orden)
# #     jefe = JefeTaller.objects.filter(id=id_sesion)
# #     jefe_sucursal = jefe[0]
# #     permisos = list(jefe_sucursal.get_all_permissions())
# #     sucursal = jefe_sucursal.sucursal
# #     ordenes = Orden.objects.filter(sucursal = sucursal)
# #     repuestos = Repuesto.objects.filter(sucursal = sucursal)
# #     form_detalle = DetalleRepuestoForm()
# #     form_detalles = []
# #     for detalle in detalles:
# #
# #         form_detalle = DetalleRepuestoForm(instance=detalle, initial=orden.__dict__)
# #         form_detalles.append(form_detalle)
# #
# #     form_detalle = DetalleRepuestoForm()
# #     form_detalles.append(form_detalle)
# #
# #     if request.method == 'POST':
# #         form_detalle= DetalleRepuestoForm(
# #             request.POST)
# #         print(form_detalle.errors)
# #         if form_detalle.is_valid():
# #             detalle = form_detalle.
# #             form_detalle.save()
# #             print(form_detalle)
# #             return HttpResponseRedirect("/reparacion/listar_ordenes")
# #
# #
# #     return render(request, 'lista_ordenes.html',
# #                   {'repuestos': repuestos, 'opcion_repuestos': True, 'permisos': permisos,
# #                    'ordenes':ordenes, 'form_detalles':form_detalles, 'detalles': detalles, 'ordenRep':ordenRep})
