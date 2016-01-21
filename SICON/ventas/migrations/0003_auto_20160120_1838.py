# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20160120_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='costo_venta',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
