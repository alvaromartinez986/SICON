from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import JsonResponse
from django.http import HttpResponse



def reporte_repuestos (request):
    sucursales = Sucursal.objects.all()
    id = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    sucursal = empleado.sucursal

    return render(request, 'reportes_repuestos.html', {'sucursales':sucursales,'sucursal':sucursal})

def data_repuestos (request):


    nombre = str (request.GET['sucursal']).strip()
    sucursal = Sucursal.objects.filter(nombre=nombre).first()
    print sucursal
    return HttpResponse("hola")
