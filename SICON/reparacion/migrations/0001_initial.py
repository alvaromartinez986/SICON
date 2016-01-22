# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 21:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleRepuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100, unique=True)),
                ('observaciones', models.TextField()),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2016, 1, 16, 21, 0, 56, 213460, tzinfo=utc))),
                ('finalizado', models.BooleanField(default=False)),
                ('fecha_fin', models.DateField(blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('mecanicos', models.ManyToManyField(to='administrador.Empleado')),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.VehiculoUsado')),
            ],
        ),
        migrations.AddField(
            model_name='detallerepuesto',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacion.Orden'),
        ),
        migrations.AddField(
            model_name='detallerepuesto',
            name='repuesto',
            field=models.ManyToManyField(to='administrador.Repuesto'),
        ),
    ]
