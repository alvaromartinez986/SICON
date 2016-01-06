# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='area',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='jefe',
            field=models.IntegerField(null=True),
        ),
    ]
