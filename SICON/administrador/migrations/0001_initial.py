# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_documento', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(max_length=20, choices=[(b'O+', b'O+'), (b'O-', b'O-'), (b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')])),
                ('experiencia', models.IntegerField()),
                ('jornada', models.CharField(max_length=15, choices=[(b'Ma\xc3\xb1ana', b'Ma\xc3\xb1ana'), (b'Tarde', b'Tarde'), (b'Noche', b'Noche')])),
                ('fecha_vinculacion', models.DateField(blank=True)),
                ('cargo', models.CharField(max_length=150, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente'), (b'Mec\xc3\xa1nico', b'Mec\xc3\xa1nico')])),
                ('telefono', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=15, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('fecha_nacimiento', models.DateField()),
                ('area', models.CharField(max_length=150)),
                ('estado_empleado', models.CharField(max_length=15, choices=[(b'Activado', b'Activado'), (b'Desactivado', b'Desactivado')])),
                ('jefe', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=40)),
                ('nombre', models.CharField(unique=True, max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('costo', models.IntegerField(null=True, blank=True)),
                ('marca_carro', models.CharField(max_length=40)),
                ('modelo_carro', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.TextField(max_length=150)),
                ('ciudad', models.ForeignKey(to='administrador.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='administrador.Empleado')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            bases=('administrador.empleado',),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
    ]
