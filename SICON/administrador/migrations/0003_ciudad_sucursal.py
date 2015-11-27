# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20151029_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
                ('departamento_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.TextField(max_length=150)),
                ('ciudad', models.ForeignKey(to='administrador.Ciudad')),
            ],
        ),
    ]
