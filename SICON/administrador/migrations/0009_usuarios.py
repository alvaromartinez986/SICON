# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_auto_20151127_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Empleado')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            bases=('administrador.empleado',),
        ),
    ]
