# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 23, 18, 36, 32, 647000, tzinfo=utc)),
        ),
    ]
