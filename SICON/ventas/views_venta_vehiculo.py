from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrador.models import VehiculoNuevo
from models import Cliente
from models import Venta
from administrador.models import VehiculoNuevo
from forms_cliente import ClienteForm
import datetime
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def venta_vehiculos(request, id_cliente):
    if request.method=='POST':
        vehiculos = request.POST.getlist('carros')
        veh_report = vehiculos
        cliente = Cliente.objects.filter(id=id_cliente).first()
        fecha = datetime.datetime.now()

        print cliente
        for vehiculo in vehiculos:
            veh_nuevo = VehiculoNuevo.objects.filter(id=vehiculo).first()
            venta = Venta (identificacion_cliente = cliente,vehiculo=veh_nuevo,fecha=fecha)
            veh_nuevo.vendido = True
            veh_nuevo.save()
            venta.save()
        return pdf_venta(veh_report,id_cliente)
        # return HttpResponseRedirect('/ventas/venta/cliente')

    vehiculos_n = VehiculoNuevo.objects.all()
    cliente = Cliente.objects.filter(id=id_cliente).first()
    return render(request,'venta_vehiculos.html',{'vehiculos_nuevos':vehiculos_n , 'cliente': cliente})

def gestionar_cliente_venta (request, identificacion):
    cliente = Cliente.objects.filter(identificacion=identificacion).first()
    print(Cliente)
    if cliente!=None:
        form=ClienteForm(instance=cliente, initial=cliente.__dict__)
        if request.method == 'POST':
            form=ClienteForm(request.POST, instance=cliente, initial=cliente.__dict__)
            if form.has_changed():
                if form.is_valid():
                    cliente =form.save()
            return HttpResponseRedirect("../venta/vehiculos/"+str(cliente.id))
    else:
        form=ClienteForm(initial={'identificacion': identificacion})
        if request.method == 'POST':
            form=ClienteForm(request.POST)
            if form.is_valid():
                cliente =form.save()
                return HttpResponseRedirect("../venta/vehiculos/"+str(cliente.id))

    return render(request, 'info_cliente_venta.html', {'sig': True, 'form': form})



def id_cliente_venta(request):
    return render(request,'info_cliente_venta.html')

def pdf_venta (vehiculos,cliente):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
