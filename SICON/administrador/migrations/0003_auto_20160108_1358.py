# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160107_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'permissions': (('listar_Empleados', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='gerente',
            options={'permissions': (('listar_Gerente', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='jefetaller',
            options={'permissions': (('listar_Jefe_Taller', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='repuesto',
            options={'permissions': (('listar_Repuestos', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'permissions': (('listar_Sucursales', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='vehiculonuevo',
            options={'permissions': (('listar_Vehiculo_Nuevo', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='vehiculousado',
            options={'permissions': (('listar_Vehiculo_Usado', 'Se permite editar, activar , desactivar'),)},
        ),
        migrations.AlterModelOptions(
            name='vendedor',
            options={'permissions': (('listar_Vendedor', 'Se permite editar, activar , desactivar'),)},
        ),
    ]
