from django.shortcuts import render
from .forms import VehiculoNuevoForm, VehiculoUsadoForm
from django.http import HttpResponseRedirect
from .models import VehiculoNuevo,VehiculoUsado, Empleado, Gerente

def crear_vehiculo_nuevo(request):
    vehiculo_n = VehiculoNuevoForm()
    exito = False
    if request.method=='POST':
        vehiculo_n = VehiculoNuevoForm(request.POST)
        id = request.session["id"]
        id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
        empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    if vehiculo_n.is_valid():
        veh = vehiculo_n.save(commit=False)
        veh.sucursal = empleado.sucursal
        veh.save()
        exito = True
        return HttpResponseRedirect('/vehiculos_nuevos/listarvn')
    return render(request, 'crear_vehiculo_nuevo.html', {'form':vehiculo_n,'exito':exito} )

def listar_vehiculos_nuevos(request):
    id = request.session["id"]
    id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
    empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    vehiculos_n = VehiculoNuevo.objects.filter(sucursal=empleado.sucursal)
    return render(request,'lista_vehiculos_nuevos.html',{'vehiculos_nuevos':vehiculos_n })

def editar_vehiculo_nuevo(request, id):
    id = request.session["id"]
    id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
    empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    vehs_n = VehiculoNuevo.objects.filter(sucursal=empleado.sucursal)
    veh_n = VehiculoNuevo.objects.get(id = id)
    form_edicion = VehiculoNuevoForm(instance=veh_n, initial=veh_n.__dict__)
    if request.method == 'POST':
        form_edicion = VehiculoNuevoForm(request.POST, instance=veh_n, initial=veh_n.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
        return HttpResponseRedirect("/vehiculos_nuevos/listarvn")
    return render(request, 'lista_vehiculos_nuevos.html', {'vehiculos_nuevos': vehs_n, 'edicion': True, 'form_edicion': form_edicion})

def eliminar_vehiculo_nuevo(request, id):
    veh_n = VehiculoNuevo.objects.get(id=id)
    if veh_n.activo:
        veh_n.activo=False
    else:
        veh_n.activo=True
    veh_n.save()
    return HttpResponseRedirect("/vehiculos_nuevos/listarvn")


def crear_vehiculo_usado(request):
    vehiculo_u = VehiculoUsadoForm()
    exito = False
    if request.method=='POST':
        vehiculo_u = VehiculoUsadoForm(request.POST)
        id = request.session["id"]
        id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
        empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    if vehiculo_u.is_valid():
        veh = vehiculo_u.save()
        veh.sucursal = empleado.sucursal
        veh.save()
        exito = True
        return HttpResponseRedirect('/vehiculos_usados/listarvu')
    return render(request, 'crear_vehiculo_usado.html', {'form':vehiculo_u,'exito':exito} )

def listar_vehiculos_usados(request):
    id = request.session["id"]
    id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
    empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    vehiculos_u = VehiculoUsado.objects.filter(sucursal=empleado.sucursal)
    return render(request,'lista_vehiculos_usados.html',{'vehiculos_usados':vehiculos_u })

def editar_vehiculo_usado(request, id):
    id = request.session["id"]
    id_empleado = Gerente.objects.filter (user_ptr_id = id).first().empleado_ptr_id
    empleado = Empleado.objects.filter (emp_id = id_empleado).first()
    vehs_u = VehiculoUsado.objects.filter(sucursal=empleado.sucursal)
    veh_u = VehiculoUsado.objects.get(id = id)
    form_edicion = VehiculoUsadoForm(instance=veh_u, initial=veh_u.__dict__)
    if request.method == 'POST':
        form_edicion = VehiculoUsadoForm(request.POST, instance=veh_u, initial=veh_u.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
		return HttpResponseRedirect("/vehiculos_usados/listarvu")
	return render(request, 'lista_vehiculos_usados.html', {'vehiculos_usados': vehs_u, 'edicion': True, 'form_edicion': form_edicion})

def eliminar_vehiculo_usado(request, id):
    veh_u = VehiculoUsado.objects.get(id=id)
    if veh_u.activo:
        veh_u.activo=False
    else:
        veh_u.activo=True
    veh_u.save()
    return HttpResponseRedirect("/vehiculos_usados/listarvu")