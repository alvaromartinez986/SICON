from django.shortcuts import render
from .forms import RepuestoForm
from django.http import HttpResponseRedirect
from .models import Repuesto
# Create your views here.
def crear_repuesto(request):
	repuesto = RepuestoForm()
	exito = False
	if request.method=='POST':
		repuesto = RepuestoForm(request.POST)
	if repuesto.is_valid():
		repuesto.save()
		exito = True
		repuesto = RepuestoForm()
		return HttpResponseRedirect('/repuestos/')
	return render(request, 'crear_repuesto.html', {'form':repuesto,'exito':exito} )

def listar_repuestos(request):
	repuestos = Repuesto.objects.all()
	return render(request,'lista_repuestos.html',{'repuestos':repuestos})

def editar_repuesto(request, id):
	print (id)
	repuestos= Repuesto.objects.all()
	repuesto = Repuesto.objects.get(pk = id)
	form_edicion = RepuestoForm(instance=repuesto, initial=repuesto.__dict__)
	if request.method == 'POST':
		form_edicion = RepuestoForm(request.POST, instance=repuesto, initial=repuesto.__dict__)
		if form_edicion.has_changed():
			if form_edicion.is_valid():
				form_edicion.save()
				return HttpResponseRedirect("/repuestos")
		else:
			return HttpResponseRedirect("/repuestos")
	return render(request, 'lista_repuestos.html', {'repuestos': repuestos, 'edicion': True, 'form_edicion': form_edicion})
