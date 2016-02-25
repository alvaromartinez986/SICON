# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160223_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculonuevo',
            old_name='fecha_ingresa',
            new_name='fecha_ingreso',
        ),
    ]
