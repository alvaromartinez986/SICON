from django.shortcuts import render
from .forms_empleado import EmpleadoForm, JefeTallerForm, GerenteForm, SuperAdminForm, VendedorForm
from django.http import HttpResponseRedirect
from .models import Empleado, Gerente, SuperAdmin, JefeTaller, Vendedor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,is_password_usable
from django.contrib.auth.decorators import login_required,permission_required
from .models import Sucursal
from django.http import JsonResponse



def reporte_repuestos (request):
    return render(request, 'reportes_repuestos.html')