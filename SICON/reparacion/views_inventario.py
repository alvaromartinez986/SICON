__author__ = 'alvaro'

from .models import Inventario
from SICON.administrador.models import Repuesto
from django.db import transaction

# metodo que modifica la cantidad del repuesto y crea el registro en el inventario

@transaction.atomic
def registro_inventario (repuesto, tipo_mvto, cantidad):

    cantidad_anterior = repuesto.cantidad
    cantidad_actual = 0
    if  (tipo_mvto == "entrada"):
        cantidad_actual =  int (repuesto.cantidad) + int (cantidad)

    else :
        cantidad_actual = int (repuesto.cantidad) - int (cantidad)


    repuesto.cantidad = cantidad_actual
    repuesto.save()
    mvto = Inventario (repuesto = repuesto,tipo_movimiento = tipo_mvto,cantidad = cantidad,
                           cantidad_anterior = cantidad_anterior , cantidad_actual = cantidad_actual)
    mvto.save()
    transaccion = transaction.savepoint()
    transaction.savepoint_commit(transaccion)









