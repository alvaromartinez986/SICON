# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20151206_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
