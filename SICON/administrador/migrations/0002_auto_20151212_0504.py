# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='jornada',
            field=models.CharField(max_length=15, choices=[(b'Manana', b'Ma\xc3\xb1ana'), (b'Tarde', b'Tarde'), (b'Noche', b'Noche')]),
        ),
    ]
