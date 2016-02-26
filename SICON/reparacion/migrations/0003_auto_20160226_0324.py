# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0002_auto_20160226_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 26, 3, 24, 29, 91243, tzinfo=utc)),
        ),
    ]
