from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Cliente
from forms_cliente import ClienteForm

from SICON.administrador.models import VehiculoNuevo, Empleado, Vendedor, Sucursal, Gerente, JefeTaller, SuperAdmin, Marca
from models import Venta, DetalleVenta
from django.db import transaction
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.db.models import Count

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, is_password_usable
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/login')
def reporte_ventas(request):
    sucursales = []

    id_sesion = request.session["id"]
    print "ID DEL USUARIO"
    print id_sesion
    gerente = Gerente.objects.filter(id=id_sesion)
    jefe = JefeTaller.objects.filter(id=id_sesion)
    vendedor = Vendedor.objects.filter(id=id_sesion)
    s_admin = SuperAdmin.objects.filter(id=id_sesion)
    sucursales = []
    sucursales2 = []
    sucursal = []

    if len(gerente)>0:
        gerente=gerente[0]
        sucursales=[gerente.sucursal]
        sucursal = sucursales[0]
    elif len(jefe)>0:
        jefe=jefe[0]
        sucursales=[jefe.sucursal]
        sucursal = sucursales[0]
    elif len(vendedor)>0:
        vendedor=vendedor[0]
        sucursales=[vendedor.sucursal]
        sucursal = sucursales [0]
    elif len(s_admin)>0:
        sucursales = Sucursal.objects.all()
        sucursal = sucursales.first()

    if len(s_admin)>0:
        sucursales2.append("Todas")

    for suc in sucursales:
        sucursales2.append(suc.nombre)


    sucursal = sucursales2[0]

    marcas = Marca.objects.all()


    return render(request, 'reportes_ventas.html', {'sucursales': sucursales2, 'sucursal': sucursal, 'marcas':marcas})

def devuelve_lineas(request):
    nombreMarca = str (request.GET['linea'])
    print nombreMarca
    lineas = VehiculoNuevo.objects.filter(marca__nombre=nombreMarca).order_by('linea').distinct('linea')
    print lineas
    dir_linea = dict()
    lista_lineas=[]
    for lineaA in lineas:
        dir_linea["nombre"] = lineaA.linea
        lista_lineas.append(dir_linea)
        dir_linea = {}
    return JsonResponse(lista_lineas, None, False)

def modelos_vendidos(request):
    print "holi"
    nombreMarca = str (request.GET['marca'])
    nombreLinea = str (request.GET['linea'])
    nombreSucursal = str(request.GET['sucursal'])
    fechaInicio = str(request.GET['inicio'])
    fechaFin = str(request.GET['fin'])
    print nombreMarca
    print nombreLinea
    print nombreSucursal
    print fechaInicio
    print fechaFin

    if fechaInicio == "":
        fechaInicio = '1999-01-01'

    if fechaFin == "":
        fechaFin = '2100-12-31'


    if nombreSucursal == "Todas":
        if nombreMarca == 'Todas':
            ventas = DetalleVenta.objects.filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).values('vehiculo__marca__nombre').annotate(total=Count('vehiculo__marca__nombre')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__marca__nombre']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}
        elif nombreLinea == 'Todas':
            ventas = DetalleVenta.objects.filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).filter(vehiculo__marca__nombre=nombreMarca).values('vehiculo__linea').annotate(total=Count('vehiculo__linea')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__linea']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}
        else:
            ventas = DetalleVenta.objects.filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).filter(vehiculo__marca__nombre=nombreMarca).filter(vehiculo__linea=nombreLinea).values('vehiculo__modelo').annotate(total=Count('vehiculo__modelo')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__modelo']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}
    else:
        if nombreMarca == 'Todas':
            ventas = DetalleVenta.objects.filter(vehiculo__sucursal__nombre=nombreSucursal).filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).values('vehiculo__marca__nombre').annotate(total=Count('vehiculo__marca__nombre')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__marca__nombre']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}
        elif nombreLinea == 'Todas':
            ventas = DetalleVenta.objects.filter(vehiculo__sucursal__nombre=nombreSucursal).filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).filter(vehiculo__marca__nombre=nombreMarca).values('vehiculo__linea').annotate(total=Count('vehiculo__linea')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__linea']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}
        else:
            ventas = DetalleVenta.objects.filter(vehiculo__sucursal__nombre=nombreSucursal).filter(id_venta_id__fecha__range=(fechaInicio, fechaFin)).filter(vehiculo__marca__nombre=nombreMarca).filter(vehiculo__linea=nombreLinea).values('vehiculo__modelo').annotate(total=Count('vehiculo__modelo')).order_by('-total')[:5]
            dir_venta = dict()
            lista_ventas=[]
            for ventaA in ventas:
                dir_venta["nombre"] = ventaA['vehiculo__modelo']
                dir_venta["valor"] = ventaA['total']
                lista_ventas.append(dir_venta)
                dir_venta = {}

    print "Esto es ventas"
    print ventas
    print "Fin ventas"

    print lista_ventas

    return JsonResponse(lista_ventas, None, False)