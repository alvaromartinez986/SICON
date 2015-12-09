# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20151130_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
