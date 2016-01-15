from django.shortcuts import render
from .forms import RepuestoForm
from django.http import HttpResponseRedirect
from .models import Repuesto, Sucursal
from views_sucursales import *
from .views_repuesto import *
from views_empleado import *
# Create your views here.


