# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0004_auto_20160206_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_fin',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 17, 8, 12, 278295, tzinfo=utc)),
        ),
    ]
