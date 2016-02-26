# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0006_auto_20160206_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 25, 22, 31, 20, 932865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orden',
            name='observaciones',
            field=models.TextField(default=datetime.datetime(2016, 2, 25, 22, 31, 42, 176356, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
