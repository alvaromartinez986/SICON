# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.CharField(blank=True, max_length=150, null=True, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente'), (b'Mecanico', b'Mec\xc3\xa1nico')]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='administrador.Sucursal', null=True),
        ),
    ]
