from django.shortcuts import render
from django.http import HttpResponseRedirect
from SICON.administrador.models import VehiculoNuevo,Empleado,Vendedor
from models import Cliente
from models import Venta,DetalleVenta
from forms_cliente import ClienteForm
from django.db import transaction
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.contrib.auth.models import User

def venta_final (request):
    if request.method=='POST':
        id = request.POST['id_cliente']
        vehiculos = request.POST.getlist('carros')
        vehiculos_sele = vehiculos
        lista_vehiculos =  []

        total = 0;
        lista_json =  []
        veh = dict()
        for vehiculo in vehiculos_sele:
            vehiculo_n = VehiculoNuevo.objects.filter(id=vehiculo).first();
            lista_vehiculos.append(vehiculo_n)
            total+= vehiculo_n.valor
            veh["cilindraje"] = str(vehiculo_n.cilindraje)
            veh["marca"] = str (vehiculo_n.marca)
            veh["linea"] = str (vehiculo_n.linea)
            veh["modelo"] = str (vehiculo_n.modelo)
            veh["tipo_comb"] = str (vehiculo_n.tipo_combustible)
            veh["color"] = str (vehiculo_n.color)
            veh["valor"] = str (vehiculo_n.valor)
            lista_json.append(veh)
            veh = {}

        lista_vehiculos = []
        resultado = dict()
        for result in resultados :
            resultado ["marca"] = result.marca
            lista_vehiculos.append(resultado)
            resultado = {}


        return render(request,'venta_final.html',{'vehiculos':lista_vehiculos,'vehiculos_json':json.dumps(lista_json),'id_cliente': id, 'total':total})

@transaction.atomic
def registrar_venta (request):
    if request.method=='POST':
        print ("metodo post")
        id = request.POST['id_cliente']
        cliente = Cliente.objects.filter(id=id).first()
        vehiculos = request.POST.getlist('codigos')
        dctos = request.POST.getlist('descuentos')

        fecha = datetime.datetime.now()
        id_vendedor = request.session["id"]
        empleado = Vendedor.objects.filter (user_ptr_id = id_vendedor).first()
        venta = Venta (identificacion_cliente = cliente,identificacion_vendedor = empleado,total = 0,fecha = fecha)
        venta.save()

        total = 0.0;
        i =0;
        lista_json =  []
        veh = dict()
        for vehiculo in vehiculos:
            veh_nuevo = VehiculoNuevo.objects.filter(codigo=vehiculo,sucursal=empleado.sucursal).first()
            print "descuento"
            print dctos[i]
            valor = float (float( veh_nuevo.valor) - float (veh_nuevo.valor * (float (dctos[i]) / 100)))
            total += valor
            detalle = DetalleVenta (id_venta = venta,vehiculo = veh_nuevo,costo=veh_nuevo.valor,dcto=(dctos[i]),costo_venta=valor)
            detalle.save()
            veh["codigo"] = str(veh_nuevo.codigo)
            veh["cilindraje"] = str(veh_nuevo.cilindraje)
            veh["marca"] = str (veh_nuevo.marca)
            veh["linea"] = str (veh_nuevo.linea)
            veh["modelo"] = str (veh_nuevo.modelo)
            veh["tipo_comb"] = str (veh_nuevo.tipo_combustible)
            veh["color"] = str (veh_nuevo.color)
            veh["valor"] = str (valor)
            lista_json.append(veh)
            veh = {}
            i+=1;
            veh_nuevo.vendido = True
            veh_nuevo.save()
        venta.total = total
        venta.save()
        sid = transaction.savepoint()
        transaction.savepoint_commit(sid)
        return render(request,'generar_pdf.html',{'vehiculos': json.dumps(lista_json),'cliente': cliente,'venta':True,'vendedor':empleado,'id':venta.id})


def venta_vehiculos(request, id_cliente):
    id = request.session["id"]
    empleado = Vendedor.objects.filter (user_ptr_id = id).first()
    vehiculos_n = VehiculoNuevo.objects.filter(activo = True, vendido = False,sucursal = empleado.sucursal)
    cliente = Cliente.objects.filter(id=id_cliente).first()
    return render(request,'venta_vehiculos.html',{'vehiculos_nuevos':vehiculos_n , 'cliente': cliente})




def gestionar_cliente_venta (request, identificacion):
    cliente = Cliente.objects.filter(identificacion=identificacion).first()
    print(Cliente)
    if cliente!=None:
        form=ClienteForm(instance=cliente, initial=cliente.__dict__)
        if request.method == 'POST':
            form=ClienteForm(request.POST, instance=cliente, initial=cliente.__dict__)
            if form.has_changed():
                if form.is_valid():
                    cliente =form.save()
            return HttpResponseRedirect("../venta/vehiculos/"+str(cliente.id))
    else:
        form=ClienteForm(initial={'identificacion': identificacion})
        if request.method == 'POST':
            form=ClienteForm(request.POST)
            if form.is_valid():
                cliente =form.save()
                return HttpResponseRedirect("../venta/vehiculos/"+str(cliente.id))

    return render(request, 'info_cliente_venta.html', {'sig': True, 'form': form})



def id_cliente_venta(request):
    return render(request,'info_cliente_venta.html')
