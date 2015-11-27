# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20151029_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cilindraje', models.IntegerField()),
                ('linea', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
                ('tipo_combustible', models.CharField(max_length=50, choices=[(b'Gasolina', b'Gasolina'), (b'Gas', b'Gas')])),
                ('color', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoNuevo',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('valor', models.IntegerField()),
            ],
            bases=('administrador.vehiculo',),
        ),
        migrations.CreateModel(
            name='VehiculoUsado',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('servicio', models.CharField(max_length=50, choices=[(b'Publico', b'Publico'), (b'Prviado', b'Privado')])),
                ('placa', models.CharField(max_length=6)),
            ],
            bases=('administrador.vehiculo',),
        ),
    ]
