# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculonuevo',
            old_name='fecha_vendido',
            new_name='fecha_ingresa',
        ),
    ]
