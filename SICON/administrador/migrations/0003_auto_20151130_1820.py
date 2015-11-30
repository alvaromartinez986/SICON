# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20151130_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculonuevo',
            name='codigo',
            field=models.CharField(default=1, unique=True, max_length=10),
        ),
    ]
