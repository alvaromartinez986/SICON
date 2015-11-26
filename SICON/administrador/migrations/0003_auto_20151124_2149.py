# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20151029_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repuesto',
            name='id',
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='codigo',
            field=models.CharField(max_length=40, unique=True, serialize=False, primary_key=True),
        ),
    ]
