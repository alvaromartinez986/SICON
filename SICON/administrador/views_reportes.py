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
from django.contrib.auth.decorators import user_passes_test

__author__ = 'nelson'

@user_passes_test(lambda u: u.has_perm('administrador.ver_reportes'),login_url="/indexAdmin")
def ver_reportes(request):
    return render(request, 'reportes.html', [])