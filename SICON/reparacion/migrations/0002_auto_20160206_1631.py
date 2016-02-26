# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
        ('reparacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallerepuesto',
            name='sucursal',
            field=models.ForeignKey(default=1, to='administrador.Sucursal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orden',
            name='sucursal',
            field=models.ForeignKey(default=1, to='administrador.Sucursal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 16, 25, 39, 850496, tzinfo=utc)),
        ),
    ]
