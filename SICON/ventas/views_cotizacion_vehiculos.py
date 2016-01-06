from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrador.models import VehiculoNuevo
from models import Cliente
from forms_cliente import ClienteForm

def cotizar_vehiculos(request):
    vehiculos_n = VehiculoNuevo.objects.all()
    return render(request,'cotizacion_vehiculos.html',{'vehiculos_nuevos':vehiculos_n })

def gestionar_cliente(request, identificacion):
    vehiculos_n= VehiculoNuevo.objects.all()
    cliente = Cliente.objects.filter(identificacion=identificacion).first()
    print(cliente)
    if cliente!=None:
        form=ClienteForm(instance=cliente, initial=cliente.__dict__)
        if request.method == 'POST':
            form=ClienteForm(request.POST, instance=cliente, initial=cliente.__dict__)
            if form.has_changed():
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("../cotizacion/vehiculos")
    else:
        form=ClienteForm()
        if request.method == 'POST':
            form=ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("../cotizacion/vehiculos")
    return render(request, 'cotizacion_vehiculos.html', {'vehiculos_nuevos': vehiculos_n, 'sig': True, 'form': form})