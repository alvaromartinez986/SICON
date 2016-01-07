from django.shortcuts import render
from .forms_orden import OrdenForm, DetalleRepuestoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Orden, DetalleRepuesto


def listar_sucursales(request):
    ordenes = Orden.objects.all()
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})


def crear_orden(request):
    orden = OrdenForm()
    exito = False
    # raise Exception{request}
    if request.method == 'POST':
        orden = OrdenForm(request.POST)
    if orden.is_valid():
        orden.save(commit=False)
        orden.estado = False
        exito = True
        orden = OrdenForm()
        print exito
    return render(request, 'crear_orden.html', {'form': orden, 'exito': exito})

#
# def editar_sucursal(request, id_sucursal):
#     sucursales = Sucursal.objects.all()
#     sucursal = Sucursal.objects.get(pk=id_sucursal)
#     ciudad = sucursal.ciudad
#     departamento = ciudad.departamento
#     form_edicion = SucursalForm(instance=sucursal, initial=sucursal.__dict__)
#     if request.method == 'POST':
#         form_edicion = SucursalForm(
#             request.POST, instance=sucursal, initial=sucursal.__dict__)
#         if form_edicion.has_changed():
#             if form_edicion.is_valid():
#                 form_edicion.save()
#                 return HttpResponseRedirect("/sucursales/listar")
#         else:
#             return HttpResponseRedirect("/sucursales/listar")
#     return render(request, 'lista_sucursales.html',
#                   {'sucursales': sucursales, 'edicion': True, 'form_edicion': form_edicion, 'departamento': departamento.id})
#
#
# def eliminar_sucursal(request, id):
#     sucursal = Sucursal.objects.get(id=id)
#     if sucursal.activo:
#         sucursal.activo = False
#     else:
#         sucursal.activo = True
#     sucursal.save()
#     return HttpResponseRedirect("/sucursales/listar")
#
#
# def cargar_ciudades(request):
#     if request.method == 'POST':
#         departamento_id = request.POST['departamento']
#         departamento_obj = Departamento.objects.get(id=departamento_id)
#         ciudades = Ciudad.objects.filter(departamento=departamento_obj)
#         lista_ciudades = []
#     dir_ciudad = dict()
#     for ciudad in ciudades:
#         dir_ciudad["id"] = str(ciudad.id)
#         dir_ciudad["nombre"] = ciudad.nombre
#         lista_ciudades.append(dir_ciudad)
#         dir_ciudad = {}
#     return JsonResponse(lista_ciudades, None, False)
