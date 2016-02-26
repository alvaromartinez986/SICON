from SICON.reparacion.models import Inventario
from SICON.administrador.models import Repuesto, Gerente, Sucursal
from django.db import transaction, connection
import datetime
from django.http import HttpResponse
import json


def mas_movimientos(request):
    id = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    sucursal=empleado.sucursal
    # sucursal  = Sucursal.objects.get(id=sucursal)
    # cursor = connection.cursor()
    # query = Inventario.objects.extra(select={"repuesto_id":"repuesto_id", "entradas":"CASE WHEN tipo_movimiento= 'entrada' THEN reparacion_inventario.cantidad ELSE 0 END", "salidas":"CASE WHEN tipo_movimiento = 'salida' THEN reparacion_inventario.cantidad ELSE 0 END"}).filter(repuesto__sucursal=sucursal)
    # fecha_inicio =request.get['inicio']
    # fecha_fin =request.get['final']
    fecha_inicio=datetime.date(2015,12,31)
    fecha_fin=datetime.date(2016,3,1)
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
        cans.append([entradas+salidas, repuesto.id])
        # print(entradas, salidas, repuesto.id)
        diccionario['id']=repuesto.id
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




        # print(que['entradas'])
        # print(que['salidas'])

#SELECT repuesto_id, SUM(CASE WHEN tipo_movimiento= 'entrada' THEN cantidad ELSE 0 END) entradas,SUM(CASE WHEN tipo_movimiento = 'salida' THEN cantidad ELSE 0 END) salidas  FROM reparacion_inventario GROUP BY repuesto_id order by sum (cantidad) desc limit 5    print (query)

    # inventarios = Inventario.objects.filter(repuesto.sucursal.id=sucursal, fecha<=fecha_fin, fecha>=fecha_ini)
    # repuestos = Repuesto.objects.filter(sucursal=sucursal).count() #no se si esta bien
    # rep_inv = [0 for c in range (repuestos)] #en la posicion i va el numero de movimientos del repuesto con id i
    # for inv in inventarios:
    #     inv.cantidad
