# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_ciudad_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
