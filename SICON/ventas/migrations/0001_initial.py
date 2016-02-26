# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(unique=True, max_length=30)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.IntegerField(null=True)),
                ('dcto', models.FloatField(null=True)),
                ('costo_venta', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(null=True)),
                ('fecha', models.DateTimeField()),
                ('identificacion_cliente', models.ForeignKey(to='ventas.Cliente')),
                ('identificacion_vendedor', models.ForeignKey(to='administrador.Empleado')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='id_venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='vehiculo',
            field=models.OneToOneField(to='administrador.VehiculoNuevo'),
        ),
    ]
