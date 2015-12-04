# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_auto_20151127_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=150),
        ),
    ]
