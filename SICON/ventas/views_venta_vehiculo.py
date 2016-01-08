from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrador.models import VehiculoNuevo
from models import Cliente
from models import Venta
from administrador.models import VehiculoNuevo
from forms_cliente import ClienteForm
import time

def venta_vehiculos(request, id_cliente):
    if request.method=='POST':
        vehiculos = request.POST.getlist('carros')
        cliente = Cliente.objects.filter(id=id_cliente).first()
        fecha = time.strftime("%c")

        print cliente
        for vehiculo in vehiculos:
            veh_nuevo = VehiculoNuevo.objects.filter(id=vehiculo).first()
            venta = Venta (identificacion_cliente = cliente,vehiculo=veh_nuevo,fecha=fecha)
            venta.save()
        return HttpResponseRedirect('/ventas/venta/cliente/')

    vehiculos_n = VehiculoNuevo.objects.all()
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