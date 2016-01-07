# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_auto_20160105_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(to='administrador.Sucursal'),
        ),
    ]
