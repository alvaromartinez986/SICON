__author__ = 'nelson'
from django.shortcuts import render

from django.http import HttpResponseRedirect
from .models import Usuarios
from .forms_usuarios import UsuariosForm

def listar_usuarios(request):
    print "hola que hace"
    usuario = Usuarios.objects.all()
    return render(request,'lista_usuarios.html',{'usuarios':usuario})


def crear_usuario(request):
    usuario = UsuariosForm()
    exito = False
    if request.method == 'POST':
        usuario = UsuariosForm(request.POST)
    if usuario.is_valid():
        usuario.save()
        exito = True
        usuario = UsuariosForm()
        return HttpResponseRedirect('/usuario/')
    return render(request, 'crear_usuario.html', {'form': usuario, 'exito': exito})

def editar_usuarios(request, id):
    print (id)
    usuarios= Usuarios.objects.all()
    usuario = Usuarios.objects.get(pk = id)
    form_edicion = UsuariosForm(instance=usuario, initial=usuario.__dict__)
    if request.method == 'POST':
        form_edicion = UsuariosForm(request.POST, instance=usuario, initial=usuario.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/usuario")

        else:
            return HttpResponseRedirect("/usuario")
    return render(request, 'lista_usuarios.html', {'usuarios': usuario, 'edicion': True, 'form_edicion': form_edicion})