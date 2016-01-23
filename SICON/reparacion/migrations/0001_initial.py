# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleRepuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=100)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2016, 1, 23, 18, 0, 2, 724650, tzinfo=utc))),
                ('finalizado', models.BooleanField(default=False)),
                ('fecha_fin', models.DateField(blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('mecanicos', models.ManyToManyField(to='administrador.Empleado')),
                ('placa', models.ForeignKey(to='administrador.VehiculoUsado')),
            ],
        ),
        migrations.AddField(
            model_name='detallerepuesto',
            name='orden',
            field=models.ForeignKey(to='reparacion.Orden'),
        ),
        migrations.AddField(
            model_name='detallerepuesto',
            name='repuesto',
            field=models.ManyToManyField(to='administrador.Repuesto'),
        ),
    ]
