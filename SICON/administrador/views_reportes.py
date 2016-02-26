__author__ = 'nelson'
from operator import is_
from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import JsonResponse
import json
from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor, Vehiculo, VehiculoNuevo, Marca, Sucursal
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import HttpResponse
from django.db.models import Count


__author__ = 'nelson'

@login_required(login_url='/login')
def ver_reportes(request):
    sucursales = Sucursal.objects.all()
    id = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    sucursal = empleado.sucursal

    return render(request, 'reportes.html', {'sucursales':sucursales,'sucursal':sucursal})

def data_vehiculos (request):

    print("ENTRO EN DATA VEHICULOS")

    nombre = str (request.GET['sucursal']).strip()
    sucursal = Sucursal.objects.filter(nombre=nombre).first()
    print ("SUCURSAL DEL FILTER: ",sucursal.id)
    fecha_inicio=str(request.GET['inicio'])
    fecha_fin=str(request.GET['fin'])

    # results = VehiculoNuevo.objects.extra(tables=["administrador_vehiculo","administrador_vehiculonuevo"],
    #                       where=["administrador_vehiculo.id = administrador_vehiculonuevo.vehiculo_ptr_id"])
    results = VehiculoNuevo.objects.filter(fecha_ingreso__range=(fecha_inicio, fecha_fin),sucursal_id=sucursal.id)
    #print(results)
    contando= VehiculoNuevo.objects.filter(fecha_ingreso__range=(fecha_inicio, fecha_fin),sucursal_id=sucursal.id).values('marca_id').annotate(total=Count('marca_id')).order_by('-total')


    print("Contando marca_id: ",contando[0]["marca_id"])
    print("Contando total: ",contando[0]["total"])
    param=contando[0]["marca_id"]
    totalingresos=contando[0]["total"]
    nombremarca=Marca.objects.filter(id=param).first()
    print("Nombre De Marca",nombremarca)

    print("Len: ",len(results))
    print("Vehiculo 1 nombre sucursal: ",results[0].sucursal.nombre)
    print("Vehiculo 1 nombre: ",results[0].marca.nombre)
    print("Vehiculo 1 fecha ingreso: ",results[0].fecha_ingreso)


    lista_vehiculos = []
    resultado = dict()
    for resulta in results :
        resultado["id"] = resulta.id
        resultado["cilindraje"] = resulta.cilindraje
        resultado["linea"] = resulta.linea
        resultado["modelo"] = resulta.modelo
        resultado["tipo_combustible"] = resulta.tipo_combustible
        resultado["colors"] = resulta.color
        resultado["marca"] = resulta.marca.nombre
        resultado["valor"] = resulta.valor
        resultado["fecha"] = str(resulta.fecha_ingreso)
        lista_vehiculos.append(resultado)
        resultado = {}




    #print("RESULTADO DE LA CONSULTA:", results)
    print ("SUCURSAL-->",sucursal)
    print ("FECHA I -->",fecha_inicio)
    print("FECHA FIN -->",fecha_fin)

    return HttpResponse(json.dumps(lista_vehiculos))
