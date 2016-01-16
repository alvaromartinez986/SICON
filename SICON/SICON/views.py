__author__ = 'nelson    '

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .singletonsesion import Sesion



def iniciar_sesion(request):
    if request.method =='POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')

        usuario = authenticate(username=usuario,password=contrasena)

        if usuario is not None:

            if usuario.is_active:
                login(request, usuario)
                return HttpResponseRedirect('indexAdmin.html')
            else:
                return render(request,'login.html',{'error':'Su cuenta se encuentra desactivada'})
        else:
            error = "Su nombre de usuario o contrasena son invalidos"
            return render(request,'login.html',{'error':error})
    else:
        return render(request,'login.html',{'error':''})
    return render(request,'login.html',{})

@login_required(login_url='/login')
def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html',{})

@login_required(login_url='/login')
def index(request):
    return render(request,'indexAdmin.html',{})