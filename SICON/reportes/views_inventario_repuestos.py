from SICON.reparacion.models import Inventario
from SICON.administrador.models import Repuesto, Gerente
from django.db import transaction, connection

def mas_movimientos(request):
    id = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    sucursal=empleado.sucursal
    cursor = connection.cursor()
    query = cursor.execute('''SELECT repuesto_id, SUM(CASE WHEN tipo_movimiento= "entrada" THEN cantidad ELSE 0 END) entradas, SUM(CASE WHEN tipo_movimiento = "salida" THEN cantidad ELSE 0 END) salidas FROM reparacion_inventario NATURAL JOIN administracion_repuesto NATURAL JOIN administracion_sucursal GROUP BY repuesto_id order by sum (cantidad) desc limit 5''')
    print (query)

    # inventarios = Inventario.objects.filter(repuesto.sucursal.id=sucursal, fecha<=fecha_fin, fecha>=fecha_ini)
    # repuestos = Repuesto.objects.filter(sucursal=sucursal).count() #no se si esta bien
    # rep_inv = [0 for c in range (repuestos)] #en la posicion i va el numero de movimientos del repuesto con id i
    # for inv in inventarios:
    #     inv.cantidad
