from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Cliente
from forms_cliente import ClienteForm

from SICON.administrador.models import VehiculoNuevo, Empleado, Vendedor, Sucursal, Gerente, Marca
from models import Venta, DetalleVenta
from django.db import transaction
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, is_password_usable
from django.contrib.auth.decorators import login_required, permission_required


def reporte_ventas(request):
    sucursales = Sucursal.objects.all()
    id = request.session["id"]
    empleado = Gerente.objects.filter(user_ptr_id=id).first()
    sucursal = empleado.sucursal

    marcas = Marca.objects.all()

    return render(request, 'reportes_ventas.html', {'sucursales': sucursales, 'sucursal': sucursal, 'marcas':marcas})

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
