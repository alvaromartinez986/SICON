# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0009_auto_20160225_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallerepuesto',
            name='sucursal',
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 26, 10, 53, 18, 300304, tzinfo=utc)),
        ),
    ]
