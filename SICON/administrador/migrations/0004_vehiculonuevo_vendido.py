# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20160108_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculonuevo',
            name='vendido',
            field=models.BooleanField(default=False),
        ),
    ]
