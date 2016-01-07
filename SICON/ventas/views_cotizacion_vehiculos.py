from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrador.models import VehiculoNuevo
from models import Cliente
from forms_cliente import ClienteForm

def cotizar_vehiculos(request):
    vehiculos_n = VehiculoNuevo.objects.all()
    return render(request,'cotizacion_vehiculos.html',{'vehiculos_nuevos':vehiculos_n })

def gestionar_cliente(request, identificacion):
    cliente = Cliente.objects.filter(identificacion=identificacion).first()
    print(Cliente)
    if cliente!=None:
        form=ClienteForm(instance=cliente, initial=cliente.__dict__)
        if request.method == 'POST':
            form=ClienteForm(request.POST, instance=cliente, initial=cliente.__dict__)
            if form.has_changed():
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("../cotizacion/vehiculos")
    else:
        form=ClienteForm(initial={'identificacion': identificacion})
        if request.method == 'POST':
            form=ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("../cotizacion/vehiculos")
    return render(request, 'info_cliente.html', {'sig': True, 'form': form})



def id_cliente(request):
    return render(request,'info_cliente.html')