# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20151212_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='no_documento',
            field=models.CharField(unique=True, max_length=40),
        ),
    ]
