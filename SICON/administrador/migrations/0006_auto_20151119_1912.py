# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_auto_20151119_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='departamento_id',
            new_name='departamento',
        ),
    ]
