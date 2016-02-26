# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0005_auto_20160206_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallerepuesto',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='estado',
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 19, 14, 14, 961154, tzinfo=utc)),
        ),
    ]
