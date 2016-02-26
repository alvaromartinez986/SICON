from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from SICON.reparacion.models import Inventario
from SICON.administrador.models import Repuesto, Gerente, Sucursal
from django.db import transaction, connection
import json

@user_passes_test(lambda u: u.has_perm('administrador.ver_reportes'),login_url="/indexAdmin")
def reporte_repuestos (request):
    sucursales = Sucursal.objects.all()
    id = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    sucursal = empleado.sucursal

    return render(request, 'reportes_repuestos.html', {'sucursales':sucursales,'sucursal':sucursal})

def mas_movimientos (request):

    nombre = str (request.GET['sucursal']).strip()
    sucursal = Sucursal.objects.filter(nombre=nombre).first()
    fecha_inicio = request.GET['inicio']
    fecha_fin = request.GET['fin']
    repuestos= Repuesto.objects.filter(sucursal=sucursal)
    cans = []
    diccionario = dict()
    lista_d = []
    for repuesto in repuestos:
        inventarios =Inventario.objects.extra(select={"repuesto_id":"repuesto_id", "entradas":"CASE WHEN tipo_movimiento= 'entrada' THEN reparacion_inventario.cantidad ELSE 0 END", "salidas":"CASE WHEN tipo_movimiento = 'salida' THEN reparacion_inventario.cantidad ELSE 0 END"}).filter(repuesto=repuesto, fecha__range=[fecha_inicio,fecha_fin])
        entradas=0
        salidas=0
        for inv in inventarios:
            entradas+=inv.entradas
            salidas+=inv.salidas
        cans.append([entradas+salidas, repuesto.nombre])
        # print(entradas, salidas, repuesto.id)
        diccionario['id']=repuesto.nombre
        diccionario['entradas']=entradas
        diccionario['salidas']=salidas
        lista_d.append(diccionario)
        diccionario={}
    # print(lista_d)
    cans.sort(key=lambda x: x[0], reverse=True)
    ids = [row[1] for row in cans][:5]
    print(ids)
    diccionario_filtrado= [dic for dic in lista_d if dic['id'] in ids]
    # diccionario_filtrado= []
    # for dic in lista_d:
    #     print(dic['id'])
    #         # diccionario_filtrado.append(dic)

    print(diccionario_filtrado)
    return HttpResponse(json.dumps(diccionario_filtrado))

