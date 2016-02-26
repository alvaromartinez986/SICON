# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gerente',
            options={'permissions': (('listar_Gerente', 'Se permite editar, activar , desactivar'), ('ver_reportes', 'permite ver los distintos reportes de la aplicacion'))},
        ),
    ]
