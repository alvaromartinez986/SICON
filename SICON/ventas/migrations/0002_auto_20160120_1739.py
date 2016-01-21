# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='costo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='costo_venta',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='dcto',
            field=models.FloatField(null=True),
        ),
    ]
