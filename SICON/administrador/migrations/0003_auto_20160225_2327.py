# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160226_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='jornada',
            field=models.CharField(default=b'Manana', max_length=15, choices=[(b'Manana', b'Ma\xc3\xb1ana'), (b'Tarde', b'Tarde'), (b'Noche', b'Noche')]),
        ),
    ]
