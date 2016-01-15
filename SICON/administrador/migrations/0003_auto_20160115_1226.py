# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_remove_vehiculo_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='sucursal',
            field=models.ForeignKey(to='administrador.Sucursal', null=True),
        ),
        migrations.AlterField(
            model_name='vehiculonuevo',
            name='codigo',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
