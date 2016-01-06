# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160105_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='jefe',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
