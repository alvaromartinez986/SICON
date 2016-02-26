# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0008_auto_20160225_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 25, 23, 31, 8, 357398, tzinfo=utc)),
        ),
    ]
