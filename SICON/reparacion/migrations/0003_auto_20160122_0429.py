# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion', '0002_auto_20160116_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 1, 22, 4, 29, 3, 622820, tzinfo=utc)),
        ),
    ]
