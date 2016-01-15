# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160115_0123'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='repuesto',
            unique_together=set([('codigo', 'sucursal')]),
        ),
    ]
