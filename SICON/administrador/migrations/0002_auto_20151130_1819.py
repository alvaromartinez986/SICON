# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculonuevo',
            name='codigo',
            field=models.CharField(default=1, unique=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiculousado',
            name='placa',
            field=models.CharField(unique=True, max_length=6),
        ),
    ]
