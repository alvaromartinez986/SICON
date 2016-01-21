# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_movimiento', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
                ('cantidad_anterior', models.IntegerField()),
                ('cantidad_actual', models.IntegerField()),
                ('repuesto', models.ForeignKey(to='administrador.Repuesto')),
            ],
        ),
    ]
