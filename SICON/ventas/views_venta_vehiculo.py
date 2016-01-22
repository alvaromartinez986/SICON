from django.shortcuts import render
from django.http import HttpResponseRedirect
from SICON.administrador.models import VehiculoNuevo
from models import Cliente
from models import Venta
from SICON.administrador.models import VehiculoNuevo
from forms_cliente import ClienteForm
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.contrib.auth.models import User

def redirect():
    return HttpResponseRedirect('/ventas/venta/cliente')

def venta_vehiculos(request, id_cliente):
    id = request.session["id"]
    vendedor = User.objects.filter (id = id).first()
    print vendedor.username
    vehiculos_n = VehiculoNuevo.objects.filter(activo = True, vendido = False)
    vehiculos_sele = ""
    cliente = Cliente.objects.filter(id=id_cliente).first()
    if request.method=='POST':
        vehiculos = request.POST.getlist('carros')
        vehiculos_sele = vehiculos
        veh_report = vehiculos
        fecha = datetime.datetime.now()

        print cliente
        for vehiculo in vehiculos:
            veh_nuevo = VehiculoNuevo.objects.filter(id=vehiculo).first()
            venta = Venta (identificacion_cliente = cliente,vehiculo=veh_nuevo,fecha=fecha)
            veh_nuevo.vendido = True
            veh_nuevo.save()
            venta.save()

        lista_vehiculos =  []
        veh = dict()
        for vehiculo in vehiculos_sele:
            vehiculo_n = veh_nuevo = VehiculoNuevo.objects.filter(id=vehiculo).first();
            veh["cilindraje"] = str(vehiculo_n.cilindraje)
            veh["marca"] = str (vehiculo_n.marca)
            veh["linea"] = str (vehiculo_n.linea)
            veh["modelo"] = str (vehiculo_n.modelo)
            veh["tipo_comb"] = str (vehiculo_n.tipo_combustible)
            veh["color"] = str (vehiculo_n.color)
            veh["valor"] = str (vehiculo_n.valor)
            lista_vehiculos.append(veh)
            veh = {}
        # return render(request,'venta_vehiculos.html',{'vehiculos_nuevos':vehiculos_n , 'cliente': cliente,'vehiculos':json.dumps(lista_vehiculos),'venta':True,'cliente':cliente, 'vendedor':"" })
        return render(request,'venta_vehiculos.html',{'vehiculos_nuevos':vehiculos_n , 'cliente': cliente,'vehiculos':json.dumps(lista_vehiculos),'venta':True,'cliente':cliente,'vendedor':vendedor})



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
