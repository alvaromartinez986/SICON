from django.shortcuts import render
from django.http import HttpResponseRedirect
from SICON.administrador.models import VehiculoNuevo
from models import Cliente
from forms_cliente import ClienteForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.has_perm('ventas.add_venta'),login_url="/indexAdmin")
def cotizar_vehiculos(request, id_cliente):
    vehiculos_n = VehiculoNuevo.objects.filter(activo = True, vendido = False)
    cliente = Cliente.objects.filter(id=id_cliente).first()
    return render(request,'cotizacion_vehiculos.html',{'vehiculos_nuevos':vehiculos_n , 'cliente': cliente})

@user_passes_test(lambda u: u.has_perm('ventas.add_cliente'),login_url="/indexAdmin")
def gestionar_cliente(request, identificacion):
    cliente = Cliente.objects.filter(identificacion=identificacion).first()
    print(Cliente)
    if cliente!=None:
        form=ClienteForm(instance=cliente, initial=cliente.__dict__)
        if request.method == 'POST':
            form=ClienteForm(request.POST, instance=cliente, initial=cliente.__dict__)
            if form.has_changed():
                if form.is_valid():
                    cliente =form.save()
            return HttpResponseRedirect("../cotizacion/vehiculos/"+str(cliente.id))
    else:
        form=ClienteForm(initial={'identificacion': identificacion})
        if request.method == 'POST':
            form=ClienteForm(request.POST)
            if form.is_valid():
                cliente =form.save()
                return HttpResponseRedirect("../cotizacion/vehiculos/"+str(cliente.id))

    return render(request, 'info_cliente.html', {'sig': True, 'form': form})


@user_passes_test(lambda u: u.has_perm('ventas.add_cliente'),login_url="/indexAdmin")
def id_cliente(request):
    return render(request,'info_cliente.html')